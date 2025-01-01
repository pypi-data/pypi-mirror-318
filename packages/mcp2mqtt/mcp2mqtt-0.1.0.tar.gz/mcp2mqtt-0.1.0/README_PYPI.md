# mcp2mqtt: Bridge between AI Models and Physical World

Connect AI Large Language Models to hardware devices through the Model Context Protocol (MCP).

[GitHub Repository](https://github.com/mcp2everything/mcp2mqtt) | [Documentation](https://github.com/mcp2everything/mcp2mqtt/tree/main/docs)

## Features

- **Intelligent Serial Communication**
  - Automatic port detection and configuration
  - Multiple baud rate support (default 115200)
  - Real-time status monitoring and error handling

- **MCP Protocol Integration**
  - Full Model Context Protocol support
  - Resource management and tool invocation
  - Flexible prompt system

## Supported Clients

mcp2mqtt supports all clients implementing the MCP protocol, including:

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
        "mcp2mqtt": {
            "command": "uvx",
            "args": ["mcp2mqtt"]
        }
    }
}
```

## MQTT and command Configuration
Create or modify `config.yaml` to configure mqtt parameters:

```yaml
mqtt:
  # MQTT服务器配置 - 使用EMQX公共测试服务器
  broker: "broker.emqx.io"  # EMQX公共测试服务器地址
  port: 1883  # TCP端口
  websocket_port: 8083  # WebSocket端口
  ssl_port: 8883  # SSL/TLS端口
  ws_ssl_port: 8084  # WebSocket Secure端口
  quic_port: 14567  # QUIC端口
  client_id: "mcp2mqtt_test_client"  # 测试客户端ID
  username: ""  # 公共测试服务器不需要认证
  password: ""  # 公共测试服务器不需要认证
  keepalive: 60
  response_start_string: "CMD"  # 应答的开始字符串，用于验证响应

# MCP工具定义
tools:
  set_pwm:
    name: "set_pwm"
    description: "设置PWM频率，范围0-100"
    parameters:
      - name: "frequency"
        type: "integer"
        description: "PWM频率值(0-100)"
        required: true
    mqtt_topic: "mcp2mqtt/pwm"
    response_topic: "mcp2mqtt/pwm/response"
    response_format: "CMD PWM {frequency} OK"
```
## Configuration File Location

The configuration file (`config.yaml`) can be placed in different locations depending on your needs. The program searches for the configuration file in the following order:

### 1. Current Working Directory (For Development)
- Path: `./config.yaml`
- Example: If you run the program from `C:\Projects`, it will look for `C:\Projects\config.yaml`
- Best for: Development and testing
- No special permissions required

### 2. User's Home Directory (Recommended for Personal Use)
- Windows: `C:\Users\YourName\.mcp2mqtt\config.yaml`
- macOS: `/Users/YourName/.mcp2mqtt/config.yaml`
- Linux: `/home/username/.mcp2mqtt/config.yaml`
- Best for: Personal configuration
- Create the `.mcp2mqtt` directory if it doesn't exist
- No special permissions required

### 3. System-wide Configuration (For Multi-user Setup)
- Windows: `C:\ProgramData\mcp2mqtt\config.yaml` (requires admin rights)
- macOS/Linux: `/etc/mcp2mqtt/config.yaml` (requires sudo/root)
- Best for: Shared configuration in multi-user environments
- Create the directory with appropriate permissions

The program will use the first valid configuration file it finds in this order. Choose the location based on your needs:
- For testing: use current directory
- For personal use: use home directory (recommended)
- For system-wide settings: use ProgramData or /etc

## Documentation

For detailed documentation, please visit our [GitHub repository](https://github.com/mcp2everything/mcp2mqtt).

## Support

If you encounter any issues or have questions:
1. Check our [Issues](https://github.com/mcp2everything/mcp2mqtt/issues) page
2. Read our [Wiki](https://github.com/mcp2everything/mcp2mqtt/wiki)
3. Create a new issue if needed

## License

This project is licensed under the MIT License.
