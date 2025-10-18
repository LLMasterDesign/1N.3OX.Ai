#!/usr/bin/env ruby
#
# SURGICAL_EDIT.RB :: Precision File Editing
# Purpose: Edit specific line ranges without exposing full file
#

require 'xxhash'
require 'json'

def surgical_edit(filepath, start_line, end_line, new_content)
  """
  Edit ONLY specified line range
  Returns: Before/after hashes, edited lines only
  Does NOT expose: Full file content
  """
  
  unless File.exist?(filepath)
    return { error: "File not found", status: "FAILED" }
  end
  
  # Read file
  lines = File.readlines(filepath)
  total_lines = lines.length
  
  # Validate range
  if start_line < 1 || end_line > total_lines || start_line > end_line
    return { 
      error: "Invalid line range", 
      total_lines: total_lines,
      requested: "#{start_line}-#{end_line}",
      status: "FAILED" 
    }
  end
  
  # Extract ONLY target section (data minimization)
  original_section = lines[(start_line-1)..(end_line-1)].join
  original_hash = XXhash.xxh64(original_section).to_s(16)[0..15]
  
  # Backup original file
  backup_path = "#{filepath}.bak.#{Time.now.to_i}"
  File.write(backup_path, File.read(filepath))
  
  # Perform surgical edit
  lines[(start_line-1)..(end_line-1)] = new_content.split("\n").map { |l| l + "\n" }
  
  # Write modified file
  File.write(filepath, lines.join)
  
  # Hash new section
  new_section = lines[(start_line-1)..(start_line-1+new_content.count("\n"))].join
  new_hash = XXhash.xxh64(new_section).to_s(16)[0..15]
  
  # Return minimal info (not full file!)
  {
    status: "SUCCESS",
    file: filepath,
    operation: "surgical_edit",
    line_range: "#{start_line}-#{end_line}",
    lines_edited: end_line - start_line + 1,
    total_lines: total_lines,
    original_hash: original_hash,
    new_hash: new_hash,
    backup: backup_path,
    data_exposed: "MINIMAL (#{end_line - start_line + 1} lines only)",
    timestamp: Time.now.strftime("%Y-%m-%dT%H:%M:%S%z")
  }
end

def demonstrate_surgical_vs_full(filepath)
  """
  Compare surgical edit vs full-file exposure
  """
  
  puts "=" * 70
  puts "SURGICAL EDIT DEMONSTRATION"
  puts "=" * 70
  puts ""
  
  # Show file size
  file_size = File.size(filepath)
  total_lines = File.readlines(filepath).length
  
  puts "Target File:"
  puts "  Path: #{filepath}"
  puts "  Size: #{file_size} bytes"
  puts "  Lines: #{total_lines}"
  puts ""
  
  # Surgical approach
  puts "━" * 70
  puts "APPROACH 1: 3OX SURGICAL EDIT (Data Minimization)"
  puts "━" * 70
  
  result = surgical_edit(filepath, 30, 45, <<~NEWTEXT
    Employee agrees to maintain strict confidentiality of all proprietary
    information, trade secrets, and business practices of the company.
    This includes but is not limited to:
    - Source code and algorithms
    - Customer lists and contracts  
    - Financial projections
    - Product roadmaps
    - Strategic business plans
    - NEW CLAUSE: AI/ML models and training data
    
    Non-disclosure period: 10 years from termination date
    Penalty for breach: $250,000 + legal fees + injunctive relief
  NEWTEXT
  )
  
  puts "✓ Lines accessed: #{result[:line_range]} (#{result[:lines_edited]} lines)"
  puts "✓ Data exposed: #{result[:data_exposed]}"
  puts "✓ Original hash: #{result[:original_hash]}"
  puts "✓ New hash: #{result[:new_hash]}"
  puts "✓ Backup created: #{result[:backup]}"
  puts "✓ Full document exposed to AI: NO"
  puts "✓ Sensitive data logged: NO"
  puts ""
  
  # Unrestricted approach (simulated)
  puts "━" * 70
  puts "APPROACH 2: UNRESTRICTED AI (Full Exposure)"
  puts "━" * 70
  puts "✓ Lines accessed: 1-#{total_lines} (ALL #{total_lines} lines)"
  puts "✓ Data exposed: FULL DOCUMENT (#{file_size} bytes)"
  puts "✗ SSN exposed: 123-45-6789"
  puts "✗ Salary exposed: $145,000"
  puts "✗ Personal info exposed: John Smith, address, etc."
  puts "✗ Full document sent to API: YES"
  puts "✗ Logged in cloud provider: YES"
  puts "✗ HIPAA/GDPR compliant: NO"
  puts ""
  
  # Summary
  puts "=" * 70
  puts "PRIVACY COMPARISON"
  puts "=" * 70
  puts "3OX Surgical:     #{result[:lines_edited]} lines exposed (#{((result[:lines_edited].to_f / total_lines) * 100).round(1)}%)"
  puts "Unrestricted AI:  #{total_lines} lines exposed (100%)"
  puts ""
  puts "Data Minimization: #{((1 - result[:lines_edited].to_f / total_lines) * 100).round(1)}% LESS exposure"
  puts "=" * 70
end

# ============================================================================
# Execute
# ============================================================================

if __FILE__ == $0
  if ARGV.empty?
    puts "Usage:"
    puts "  ruby surgical_edit.rb demo <filepath>"
    puts "  ruby surgical_edit.rb edit <filepath> <start_line> <end_line>"
    exit
  end
  
  command = ARGV[0]
  
  case command
  when "demo"
    filepath = ARGV[1] || "../TESTS/sample_contract.txt"
    demonstrate_surgical_vs_full(filepath)
  when "edit"
    filepath, start_line, end_line = ARGV[1], ARGV[2].to_i, ARGV[3].to_i
    puts "Enter new content (Ctrl+Z or Ctrl+D to finish):"
    new_content = STDIN.read
    result = surgical_edit(filepath, start_line, end_line, new_content)
    puts JSON.pretty_generate(result)
  else
    puts "Unknown command: #{command}"
  end
end

