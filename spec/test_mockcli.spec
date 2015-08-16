require 'arista/mockcli'
require 'json'

describe 'MockCli' do

  let (:cli) { MockCli.new }
  let (:user) { "test"}
  let (:password) { "password"}
  let (:role) { "network-admin"}

  it 'MockCli#initalize' do
    expect(cli.default?).to be true
  end

  it 'MockCli#enable' do
    cli.run(['enable'])
    expect(cli.enable?).to be true
  end

  it 'MockCli#show version' do
    cli.run(['enable'])
    expect(cli.enable?).to be true
    response = cli.run(['show version'])
    expect(response).to eq 'version'
  end

  it 'MockCli#configure error' do
    cli.run(['configure'])
    expect(cli.configure?).to be false
  end

  it 'MockCli#configure success' do
    cli.run(['enable'])
    cli.run(['configure'])
    expect(cli.configure?).to be true
  end

  it 'MockCli#configure invalid' do
    cli.run(['enable'])
    response = cli.run(['configuremispelled'])
    expect(response).to eq 'Invalid input'
  end

  it 'MockCli#username error' do
    cli.run(['enable'])
    cli.run(['configure'])
    response = cli.run(['username'])
    expect(response).to eq 'Incomplete command'
  end

  it 'MockCli#username success with number in name' do
    cli.run(['enable'])
    cli.run(['configure'])
    cmd = "username #{user} role #{role} secret 0 #{password}"
    response = cli.run([cmd])
    expect(response).to eq ''
  end

  it 'MockCli#username success' do
    cli.run(['enable'])
    cli.run(['configure'])
    cmd = "username #{user} role #{role} secret 0 #{password}"
    response = cli.run([cmd])
    expect(response).to eq ''
  end

  it 'MockCli#username sshkey successful' do
    sshkey = "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA2zGA/4TgBKdcwQQewyIvlXUQ62yV0kxxUFSV+sGzDxzpE6zK+pJj2DZlrKt6i3om3eMFSOd2MV45C/YFvaxe73ufipRQ7hvzlWMWB7MgCHygWW3qJGX/3qix/AvQU4mr4iWIG/Uin169Cdk93Siv7IRXf5tGE6nw6O1nTNONT5M188AgWRH48P9kQ4wotSlPn5Msy7F/ZTf6Vnqq9yj/3rQzob2pm+DSW9xsXIrz/hjadSjhV7rn0Yh3appIjOxigfFmFjpNHyzb2KUpRq2QT606vAMlk88QcoK7kyTsJ/oN7IG9Ekh3IIURXTeFs/EW+AmfrtFeV3KoMXf6jFdDAw== bnguyen@zero"

    cli.run(['enable'])
    cli.run(['configure'])
    cmd = "username #{user} sshkey #{sshkey}"
    response = cli.run([cmd])
    expect(response).to eq ''
  end

  it 'MockCli#username sshkey invalid key' do
    sshkey = "ssh-rsa IwAAAQEA2zGA/4TgBKdcwQQewyIvlXUQ62yV0kxxUFSV+sGzDxzpE6zK+pJj2DZlrKt6i3om3eMFSOd2MV45C/YFvaxe73ufipRQ7hvzlWMWB7MgCHygWW3qJGX/3qix/AvQU4mr4iWIG/Uin169Cdk93Siv7IRXf5tGE6nw6O1nTNONT5M188AgWRH48P9kQ4wotSlPn5Msy7F/ZTf6Vnqq9yj/3rQzob2pm+DSW9xsXIrz/hjadSjhV7rn0Yh3appIjOxigfFmFjpNHyzb2KUpRq2QT606vAMlk88QcoK7kyTsJ/oN7IG9Ekh3IIURXTeFs/EW+AmfrtFeV3KoMXf6jFdDAw== bnguyen@zero"

    cli.run(['enable'])
    cli.run(['configure'])
    cmd = "username #{user} sshkey #{sshkey}"
    response = cli.run([cmd])
    expect(response).to eq 'Unrecognized ssh key'
  end

  it 'MockCli#username success' do
    cli.run(['enable'])
    cli.run(['configure'])
    cmd = "username #{user} role #{role} secret 0 #{password}"
    response = cli.run([cmd])
    expect(response).to eq ''
  end

  it 'MockCli#username success' do
    cli.run(['enable'])
    cli.run(['configure'])
    cmd = "username #{user} role #{role} secret 0 #{password}"
    response = cli.run([cmd])
    expect(response).to eq ''
  end

  it 'MockCli#show running-config' do
    cli.run(['enable'])
    cli.run(['configure'])
    cmd = "username #{user} role #{role} secret 0 #{password}"
    cli.run([cmd])
    response = cli.run(['show running-config'])
    puts response
    expect(response).to eq [cmd]
  end
end
