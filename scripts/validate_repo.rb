#!/usr/bin/env ruby
# frozen_string_literal: true

require "json"
require "pathname"
require "yaml"

ROOT = Pathname.new(__dir__).parent
ERRORS = []

ALLOWED_FACT_STATUS = %w[VERIFIED PLANNED TO_VERIFY EXCLUDED].freeze
ALLOWED_EVIDENCE_STATUS = %w[VERIFIED TO_VERIFY NOT_PROVIDED].freeze
ALLOWED_LIFECYCLE_STATUS = %w[
  ACTIVE
  ARCHITECTURE_DESIGN
  COMPLETED
  DEMO_LEVEL_COMPLETED
  PLANNED
].freeze
ALLOWED_ACTIVITY_STATE = %w[ACTIVE_RESEARCH_INITIATIVE].freeze

EXPECTED_PRIORITY = [
  "AEGIS",
  "MITRA",
  "Skin Disease Classification",
  "NexCast Pro",
  "VisionPay",
  "Automotive BCM",
  "Smart Wellness Desk Assistant"
].freeze

EXPECTED_AEGIS_SEQUENCE = [
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
].freeze

EXPECTED_AEGIS_CANONICAL_TEXT = EXPECTED_AEGIS_SEQUENCE.join(" → ")
EXPECTED_AEGIS_RESPONSIBILITY = {
  "ai" => "Sense → Analyze → Recommend",
  "human" => "Review → Decide → Dispatch",
  "aegis" => "Record → Track → Learn"
}.freeze

PROJECT_FACTS = {
  "projects/AEGIS/facts.yaml" => "ARCHITECTURE_DESIGN",
  "projects/MITRA/facts.yaml" => "COMPLETED",
  "projects/Skin-Disease-Classification/facts.yaml" => "DEMO_LEVEL_COMPLETED",
  "projects/NexCast-Pro/facts.yaml" => "COMPLETED",
  "projects/VisionPay/facts.yaml" => "COMPLETED",
  "projects/Automotive-BCM/facts.yaml" => "COMPLETED",
  "projects/Smart-Wellness-Desk-Assistant/facts.yaml" => "COMPLETED"
}.freeze

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

def scalar?(value)
  value.is_a?(String) || value.is_a?(Numeric) || value == true || value == false || value.nil?
end

def walk_statuses(value, path, trail = [])
  case value
  when Hash
    value.each do |key, child|
      child_trail = trail + [key]
      case key
      when "fact_status"
        error("Invalid fact_status in #{path} at #{child_trail.join(".")}: #{child}") unless ALLOWED_FACT_STATUS.include?(child.to_s)
      when "evidence_status"
        error("Invalid evidence_status in #{path} at #{child_trail.join(".")}: #{child}") unless ALLOWED_EVIDENCE_STATUS.include?(child.to_s)
      when "lifecycle_status"
        error("Invalid lifecycle_status in #{path} at #{child_trail.join(".")}: #{child}") unless ALLOWED_LIFECYCLE_STATUS.include?(child.to_s)
      when "proficiency_status"
        error("Invalid proficiency_status in #{path} at #{child_trail.join(".")}: #{child}") unless ALLOWED_FACT_STATUS.include?(child.to_s)
      when "activity_state"
        error("Invalid activity_state in #{path} at #{child_trail.join(".")}: #{child}") unless ALLOWED_ACTIVITY_STATE.include?(child.to_s)
      when "status"
        if scalar?(child) && ALLOWED_FACT_STATUS.include?(child.to_s)
          # Legacy/generic status fields are allowed only for non-project helper facts.
        end
      end
      walk_statuses(child, path, child_trail)
    end
  when Array
    value.each_with_index { |child, index| walk_statuses(child, path, trail + [index]) }
  end
end

required_dirs = %w[
  profile
  skills
  projects
  experience
  leadership
  memberships
  certifications
  achievements
  placement
  roadmap
  healthcare-research
  resume
  docs
  scripts
]

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
  roadmap/README.md
  roadmap/roadmap-analysis.md
  roadmap/phase1.md
  roadmap/phase1resources.md
  roadmap/phase2.md
  roadmap/phase2resources.md
  roadmap/phase3.md
  roadmap/phase3resources.md
  roadmap/phase4.md
  roadmap/phase4resources.md
  roadmap/phase5.md
  roadmap/phase5resources.md
  roadmap/phase6.md
  roadmap/phase6resources.md
  roadmap/projects.md
  roadmap/updated_resume.md
  healthcare-research/README.md
  healthcare-research/research-state.yaml
  resume/instructions.md
  docs/DATA_GOVERNANCE.md
  docs/AI_USAGE.md
  docs/REPO_SCHEMA.md
  docs/PROJECT_STATUS.md
  docs/SOURCE_INDEX.md
  docs/CHANGELOG.md
]

required_dirs.each do |path|
  error("Missing required directory: #{path}") unless ROOT.join(path).directory?
end

required_files.each do |path|
  error("Missing required file: #{path}") unless ROOT.join(path).file?
end

yaml_files = Dir.glob(ROOT.join("**", "*.y{a,}ml")).map { |p| Pathname.new(p).relative_path_from(ROOT).to_s }
json_files = Dir.glob(ROOT.join("**", "*.json")).map { |p| Pathname.new(p).relative_path_from(ROOT).to_s }

yaml_data = yaml_files.to_h { |path| [path, yaml_load(path)] }
json_files.each { |path| json_load(path) }
yaml_data.each { |path, data| walk_statuses(data, path) if data }

priority = yaml_data.dig("projects/project-priority.yaml", "priority")
if priority
  actual_priority = priority.sort_by { |item| item["rank"] }.map { |item| item["project"] }
  error("Project priority mismatch: #{actual_priority.inspect}") unless actual_priority == EXPECTED_PRIORITY
end

PROJECT_FACTS.each do |path, expected_lifecycle|
  project_data = yaml_data.dig(path, "project")
  unless project_data
    error("Missing project block in #{path}")
    next
  end

  error("#{path} must use fact_status: VERIFIED") unless project_data["fact_status"] == "VERIFIED"
  error("#{path} must use evidence_status: TO_VERIFY") unless project_data["evidence_status"] == "TO_VERIFY"
  error("#{path} lifecycle_status mismatch") unless project_data["lifecycle_status"] == expected_lifecycle
  error("#{path} should not use ambiguous project.status") if project_data.key?("status")
end

aegis = yaml_data["projects/AEGIS/facts.yaml"]
if aegis
  sequence = aegis.dig("baseline_architecture", "sequence")
  canonical_text = aegis.dig("baseline_architecture", "canonical_text")
  error("AEGIS baseline architecture sequence mismatch") unless sequence == EXPECTED_AEGIS_SEQUENCE
  error("AEGIS canonical architecture text mismatch") unless canonical_text == EXPECTED_AEGIS_CANONICAL_TEXT
  error("AEGIS canonical architecture must use → arrows") unless canonical_text.to_s.include?("→")
  error("AEGIS team size must remain 3") unless aegis.dig("project", "team_size") == 3
  error("AEGIS code status must remain Not started") unless aegis.dig("project", "code_status") == "Not started"
  error("AEGIS hardware status must remain Not finalized") unless aegis.dig("project", "hardware_status") == "Not finalized"
  EXPECTED_AEGIS_RESPONSIBILITY.each do |key, expected|
    error("AEGIS responsibility mismatch for #{key}") unless aegis.dig("responsibility_model", key) == expected
  end
  responsibility = aegis.dig("responsibility_model", "rule").to_s
  error("AEGIS human dispatcher verification rule missing") unless responsibility.include?("human dispatcher verification")
end

mitra = yaml_data["projects/MITRA/facts.yaml"]
if mitra
  contributions = mitra.dig("ownership", "shabaz_contribution") || []
  error("MITRA navigation module contribution missing") unless contributions.include?("Navigation module")
  error("MITRA TTS contribution missing") unless contributions.include?("TTS")
  boundary = mitra.dig("ownership", "boundary", "rule").to_s
  error("MITRA backend/model boundary missing") unless boundary.include?("Do not claim Shabaz trained or developed")
end

visionpay = yaml_data["projects/VisionPay/facts.yaml"]
if visionpay
  denominations = visionpay.dig("dataset", "denominations") || []
  error("VisionPay denominations mismatch") unless denominations == ["₹10", "₹20", "₹50", "₹100", "₹200", "₹500"]
  error("VisionPay MobileNetV2 missing") unless (visionpay["known_stack"] || []).include?("MobileNetV2")
  error("VisionPay TensorFlow Lite missing") unless (visionpay["known_stack"] || []).include?("TensorFlow Lite")
  accuracy = visionpay.dig("reported_result", "validation_accuracy").to_s
  error("VisionPay accuracy wording must stay reported") unless accuracy.include?("reported approximately 93% validation accuracy")
  error("VisionPay accuracy evidence_status must be TO_VERIFY") unless visionpay.dig("reported_result", "evidence_status") == "TO_VERIFY"
  training = visionpay.dig("implementation_note", "training_code")
  error("VisionPay AI-assisted training-code note missing") unless training == "AI-assisted"
  not_completed = visionpay["not_completed"] || []
  error("VisionPay future ideas missing") unless not_completed.include?("YOLO-based detector")
end

skin = yaml_data["projects/Skin-Disease-Classification/facts.yaml"]
if skin
  contribution = skin["personal_contribution"] || []
  expected = ["Model selection", "Model training", "Model evaluation", "Python coding", "Image processing", "UI/application work", "Testing"]
  error("Skin Disease personal contribution mismatch") unless contribution == expected
  error("Skin Disease exact model must remain UNKNOWN") unless skin.dig("unknowns", "exact_model_or_algorithm") == "UNKNOWN"
end

nexcast = yaml_data["projects/NexCast-Pro/facts.yaml"]
if nexcast
  error("NexCast Pro web_ui must be VERIFIED") unless nexcast.dig("web_ui", "status") == "VERIFIED"
  unsupported_frontend = (nexcast["known_stack"] || []).grep(/React|Angular|Vue|Svelte/i)
  error("NexCast Pro has unsupported frontend framework: #{unsupported_frontend.join(", ")}") unless unsupported_frontend.empty?
end

completed = (yaml_data.dig("certifications/completed.yaml", "completed") || []).map { |item| item["name"] }
planned = (yaml_data.dig("certifications/planned.yaml", "planned") || []).map { |item| item["name"] }
overlap = completed & planned
error("Certifications appear as both completed and planned: #{overlap.join(", ")}") unless overlap.empty?

completed_statuses = yaml_data.dig("certifications/completed.yaml", "completed") || []
completed_statuses.each do |item|
  error("Completed certification must keep fact_status VERIFIED: #{item["name"]}") unless item["fact_status"] == "VERIFIED"
  error("Completed certification must keep evidence_status TO_VERIFY: #{item["name"]}") unless item["evidence_status"] == "TO_VERIFY"
end

planned_statuses = (yaml_data.dig("certifications/planned.yaml", "planned") || []).map { |item| item["status"] }.uniq
error("Planned certifications must all be PLANNED") unless planned_statuses == ["PLANNED"]

healthcare = yaml_data["healthcare-research/research-state.yaml"]
if healthcare
  error("Healthcare research must be active") unless healthcare.dig("initiative", "activity_state") == "ACTIVE_RESEARCH_INITIATIVE"
  %w[problem product architecture model dataset].each do |key|
    error("Healthcare #{key} must remain UNKNOWN") unless healthcare.dig("unknowns", key) == "UNKNOWN"
  end
end

languages = yaml_data["profile/languages.yaml"]
if languages
  (languages["languages"] || []).each do |language|
    error("Language must be fact_status VERIFIED: #{language["name"]}") unless language["fact_status"] == "VERIFIED"
    error("Language proficiency must remain TO_VERIFY: #{language["name"]}") unless language["proficiency_status"] == "TO_VERIFY"
  end
end

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
error("AI_CONTEXT missing fact_status guidance") unless context.include?("fact_status")
error("AI_CONTEXT missing evidence_status guidance") unless context.include?("evidence_status")
error("AI_CONTEXT missing ACTIVE_RESEARCH_INITIATIVE") unless context.include?("ACTIVE_RESEARCH_INITIATIVE")

excluded = read("projects/EXCLUDED.md")
error("NIDAR must be marked EXCLUDED") unless excluded.include?("Status: `EXCLUDED`")
error("Hackathon project must be marked EXCLUDED") unless excluded.include?("Hackathon Project")
error("Excluded projects must be barred from recommendations") unless excluded.include?("project recommendations")

resume = read("resume/instructions.md")
error("Resume instructions must block excluded projects") unless resume.include?("Never include excluded projects")
error("Resume instructions must block planned certifications as completed") unless resume.include?("Never mark planned certifications as completed")

if ERRORS.empty?
  puts "Validation passed."
  puts "YAML files checked: #{yaml_files.length}"
  puts "JSON files checked: #{json_files.length}"
  puts "Markdown files checked: #{markdown_files.length}"
  puts "Project lifecycle statuses checked: #{PROJECT_FACTS.length}"
else
  warn "Validation failed:"
  ERRORS.each { |message| warn "- #{message}" }
  exit 1
end
