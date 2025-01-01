# mcp2tcp: Bridge between AI Models and Physical World

Connect AI Large Language Models to hardware devices through the Model Context Protocol (MCP).

[GitHub Repository](https://github.com/mcp2everything/mcp2tcp) | [Documentation](https://github.com/mcp2everything/mcp2tcp/tree/main/docs)

## Features

- **Intelligent TCP Communication**
  - Connect and send commands to TCP server
  - Real-time status monitoring and error handling

- **MCP Protocol Integration**
  - Full Model Context Protocol support
  - Resource management and tool invocation
  - Flexible prompt system

## Supported Clients

mcp2tcp supports all clients implementing the MCP protocol, including:

- Claude Desktop (Test ok)
- Continue (Should work)
- Cline (Test ok)

## Quick Start
make sure you have installed uv
```
```bash
windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
MacOS
curl -LsSf https://astral.sh/uv/install.sh | sh
```
## Basic Configuration

Add the following to your MCP client configuration:

```json
{
    "mcpServers": {
        "mcp2tcp": {
            "command": "uvx",
            "args": ["mcp2tcp"]
        }
    }
}
```

## Serial Port Configuration

Create or modify `config.yaml` to configure serial port parameters:

```yaml
tcp:
  # TCP服务器配置
  remote_ip: "127.0.0.1"  # 远端IP地址
  port: 9999  # 端口号
  connect_timeout: 3.0  # 连接超时时间，单位为秒
  receive_timeout: 2.0  # 接收超时时间，单位为秒
  communication_type: "client"  # 通信类型，client或server
  response_start_string: "CMD"  # 可选，TCP应答的开始字符串，默认为OK

commands:
  # PWM控制命令
  set_pwm:
    command: "CMD_PWM {frequency}"  # frequency为0-100的整数，表示PWM占空比
    need_parse: false  # 不需要解析响应内容
    data_type: "ascii"  # 数据类型，ascii或hex
    parameters:
      - name: "frequency"
        type: "integer"
        description: "PWM frequency value (0-100)"
        required: true
    prompts:
      - "把PWM调到最大 (frequency=100)"
      - "把PWM调到最小 (frequency=0)"
      - "请将PWM设置为{frequency} (0-100的整数)"
      - "关闭PWM (frequency=0)"
      - "把PWM调到一半 (frequency=50)"

  # PICO信息查询命令
  get_pico_info:
    command: "CMD_PICO_INFO"  # 实际发送的命令格式，server会自动添加\r\n
    need_parse: true  # 需要解析响应内容
    data_type: "ascii"  # 数据类型，ascii或hex
    prompts:
      - "查询Pico板信息"
      - "显示开发板状态"
```

## Configuration File Location

The configuration file (`config.yaml`) can be placed in different locations depending on your needs. The program searches for the configuration file in the following order:

### 1. Current Working Directory (For Development)
- Path: `./config.yaml`
- Example: If you run the program from `C:\Projects`, it will look for `C:\Projects\config.yaml`
- Best for: Development and testing
- No special permissions required

### 2. User's Home Directory (Recommended for Personal Use)
- Windows: `C:\Users\YourName\.mcp2tcp\config.yaml`
- macOS: `/Users/YourName/.mcp2tcp/config.yaml`
- Linux: `/home/username/.mcp2tcp/config.yaml`
- Best for: Personal configuration
- Create the `.mcp2tcp` directory if it doesn't exist
- No special permissions required

### 3. System-wide Configuration (For Multi-user Setup)
- Windows: `C:\ProgramData\mcp2tcp\config.yaml` (requires admin rights)
- macOS/Linux: `/etc/mcp2tcp/config.yaml` (requires sudo/root)
- Best for: Shared configuration in multi-user environments
- Create the directory with appropriate permissions

The program will use the first valid configuration file it finds in this order. Choose the location based on your needs:
- For testing: use current directory
- For personal use: use home directory (recommended)
- For system-wide settings: use ProgramData or /etc

## Documentation

For detailed documentation, please visit our [GitHub repository](https://github.com/mcp2everything/mcp2tcp).

## Support

If you encounter any issues or have questions:
1. Check our [Issues](https://github.com/mcp2everything/mcp2tcp/issues) page
2. Read our [Wiki](https://github.com/mcp2everything/mcp2tcp/wiki)
3. Create a new issue if needed

## License

This project is licensed under the MIT License.
