require 'serverspec'

if ENV['TRAVIS']
    set :backend, :exec
end

describe 'docker Ansible role' do

    # Variable definition
    default_file = ''
    packages = Array[]
    process_name = ''
    service_name = ''

    if ['debian', 'ubuntu'].include?(os[:family])
        default_file = '/etc/default/docker'
        packages = Array[ 'docker-engine' ]
        process_name = 'docker'
        service_name = 'docker'
    end

    it 'install role packages' do
        packages.each do |pkg_name|
            expect(package(pkg_name)).to be_installed
        end
    end

    describe file(default_file) do
        it { should exist }
        it { should be_file }
        it { should be_owned_by 'root' }
        it { should be_grouped_into 'root' }
        it { should be_mode 644 }
    end

    describe service(service_name) do
        it { should be_enabled }
        it { should be_running }
    end

    describe process(process_name) do
        it { should be_running }
    end

    describe port('8081') do
        it { should be_listening }
    end
end

