require 'rake/testtask'

Rake::TestTask.new do |t|
  t.libs << "tests"
  t.test_files = FileList['tests/test*.rb']
  t.verbose = true
end

task :gem do
  system('gem build arista-eapi.gemspec')
end
