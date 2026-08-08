#!/usr/bin/env ruby
# frozen_string_literal: true

require "json"
require "pathname"
require "yaml"

ROOT = Pathname.new(__dir__).parent
ERRORS = []

def error(message)
  ERRORS << message
end

def read(path)
  ROOT.join(path).read
end

def yaml_load(path)
  YAML.load_file(ROOT.join(path))
rescue Psych::SyntaxError => e
  error("Invalid YAML: #{path}: #{e.message}")
  nil
end

def json_load(path)
  JSON.parse(ROOT.join(path).read)
rescue JSON::ParserError => e
  error("Invalid JSON: #{path}: #{e.message}")
  nil
end

required_files = %w[
  README.md
  AI_CONTEXT.md
  profile/personal.yaml
  profile/education.yaml
  profile/career-goals.yaml
  profile/languages.yaml
  skills/programming.yaml
  skills/fundamentals.yaml
  skills/hands-on.yaml
  skills/proficiency.md
  projects/project-priority.yaml
  projects/AEGIS/README.md
  projects/AEGIS/facts.yaml
  projects/MITRA/README.md
  projects/MITRA/facts.yaml
  projects/Skin-Disease-Classification/README.md
  projects/Skin-Disease-Classification/facts.yaml
  projects/NexCast-Pro/README.md
  projects/NexCast-Pro/facts.yaml
  projects/VisionPay/README.md
  projects/VisionPay/facts.yaml
  projects/Automotive-BCM/README.md
  projects/Automotive-BCM/facts.yaml
  projects/Smart-Wellness-Desk-Assistant/README.md
  projects/Smart-Wellness-Desk-Assistant/facts.yaml
  projects/EXCLUDED.md
  experience/experience-index.yaml
  leadership/positions.yaml
  memberships/memberships.yaml
  certifications/completed.yaml
  certifications/planned.yaml
  achievements/selections.yaml
  placement/strategy.md
  roadmap/progress.yaml
  healthcare-research/README.md
  healthcare-research/research-state.yaml
  resume/instructions.md
  docs/DATA_GOVERNANCE.md
  docs/AI_USAGE.md
  docs/REPO_SCHEMA.md
  docs/PROJECT_STATUS.md
  docs/CHANGELOG.md
]

required_files.each do |path|
  error("Missing required file: #{path}") unless ROOT.join(path).file?
end

yaml_files = Dir.glob(ROOT.join("**", "*.y{a,}ml")).map { |p| Pathname.new(p).relative_path_from(ROOT).to_s }
json_files = Dir.glob(ROOT.join("**", "*.json")).map { |p| Pathname.new(p).relative_path_from(ROOT).to_s }

yaml_data = yaml_files.to_h { |path| [path, yaml_load(path)] }
json_files.each { |path| json_load(path) }

expected_priority = [
  "AEGIS",
  "MITRA",
  "Skin Disease Classification",
  "NexCast Pro",
  "VisionPay",
  "Automotive BCM",
  "Smart Wellness Desk Assistant"
]

priority = yaml_data.dig("projects/project-priority.yaml", "priority")
if priority
  actual_priority = priority.sort_by { |item| item["rank"] }.map { |item| item["project"] }
  error("Project priority mismatch: #{actual_priority.inspect}") unless actual_priority == expected_priority
end

expected_aegis_sequence = [
  "Emergency",
  "Citizen/Victim",
  "SOS / Incident Report",
  "GPS / Camera / Audio inputs",
  "AEGIS Platform",
  "AI Intelligence",
  "Incident Type / Severity / Risk Factors",
  "AI Recommendation",
  "Human Dispatcher Verification",
  "Resource Selection",
  "Live Tracking",
  "Responder",
  "Incident Resolution",
  "Digital Case / Evidence / Timeline / Analytics",
  "Post-Incident Analysis"
]

aegis = yaml_data["projects/AEGIS/facts.yaml"]
if aegis
  sequence = aegis.dig("baseline_architecture", "sequence")
  error("AEGIS baseline architecture mismatch") unless sequence == expected_aegis_sequence
  error("AEGIS team size must remain 3") unless aegis.dig("project", "team_size") == 3
  error("AEGIS code status must remain Not started") unless aegis.dig("project", "code_status") == "Not started"
  error("AEGIS hardware status must remain Not finalized") unless aegis.dig("project", "hardware_status") == "Not finalized"
  responsibility = aegis.dig("responsibility_model", "rule").to_s
  error("AEGIS human dispatcher verification rule missing") unless responsibility.include?("human dispatcher verification")
end

mitra = yaml_data["projects/MITRA/facts.yaml"]
if mitra
  boundary = mitra.dig("ownership", "boundary", "rule").to_s
  error("MITRA backend/model boundary missing") unless boundary.include?("Do not claim Shabaz trained or developed")
end

visionpay = yaml_data["projects/VisionPay/facts.yaml"]
if visionpay
  training = visionpay.dig("implementation_note", "training_code")
  error("VisionPay AI-assisted training-code note missing") unless training == "AI-assisted"
  not_completed = visionpay["not_completed"] || []
  error("VisionPay roadmap items missing") unless not_completed.include?("YOLO-based detector")
end

completed = (yaml_data.dig("certifications/completed.yaml", "completed") || []).map { |item| item["name"] }
planned = (yaml_data.dig("certifications/planned.yaml", "planned") || []).map { |item| item["name"] }
overlap = completed & planned
error("Certifications appear as both completed and planned: #{overlap.join(", ")}") unless overlap.empty?

planned_statuses = (yaml_data.dig("certifications/planned.yaml", "planned") || []).map { |item| item["status"] }.uniq
error("Planned certifications must all be PLANNED") unless planned_statuses == ["PLANNED"]

all_text_files = Dir.glob(ROOT.join("**", "*")).select { |p| File.file?(p) && !p.include?("/.git/") }
secret_patterns = {
  "possible private key" => /-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----/,
  "possible GitHub token" => /gh[pousr]_[A-Za-z0-9_]{20,}/,
  "possible OpenAI key" => /sk-[A-Za-z0-9_-]{20,}/,
  "possible AWS access key" => /AKIA[0-9A-Z]{16}/
}

all_text_files.each do |file|
  content = File.binread(file)
  next if content.include?("\x00")

  relative = Pathname.new(file).relative_path_from(ROOT).to_s
  secret_patterns.each do |label, pattern|
    error("#{label} found in #{relative}") if content.match?(pattern)
  end
end

markdown_files = Dir.glob(ROOT.join("**", "*.md")).map { |p| Pathname.new(p).relative_path_from(ROOT).to_s }
markdown_link_pattern = /\[[^\]]+\]\((?!https?:\/\/|mailto:|#)([^)]+)\)/
markdown_files.each do |path|
  base = ROOT.join(path).dirname
  read(path).scan(markdown_link_pattern).flatten.each do |target|
    clean_target = target.split("#", 2).first
    next if clean_target.empty?

    target_path = base.join(clean_target).cleanpath
    error("Broken Markdown link in #{path}: #{target}") unless target_path.exist?
  end
end

context = read("AI_CONTEXT.md")
error("AI_CONTEXT missing AEGIS architecture lock") unless context.include?("AEGIS Architecture Lock")
error("AI_CONTEXT missing resume safety") unless context.include?("Resume safety")
error("AI_CONTEXT missing exclusions") unless context.include?("NIDAR")

excluded = read("projects/EXCLUDED.md")
error("NIDAR must be marked EXCLUDED") unless excluded.include?("Status: `EXCLUDED`")
error("Hackathon project must be marked EXCLUDED") unless excluded.include?("Hackathon Project")

if ERRORS.empty?
  puts "Validation passed."
  puts "YAML files checked: #{yaml_files.length}"
  puts "JSON files checked: #{json_files.length}"
  puts "Markdown files checked: #{markdown_files.length}"
else
  warn "Validation failed:"
  ERRORS.each { |message| warn "- #{message}" }
  exit 1
end
