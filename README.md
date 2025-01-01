# Parrot
Parrot is an open-source application for downloading, managing, and running various AI models.
It is designed to be a unified platform for interacting with many AI models, both open-source and propriety (via API).

## Features
- Chat with LLMs: Engage with multiple large language models in a ChatGPT-like interface.
- Open-Source Model Support: Download and run models all in one place!
- Propriety Model Integration: Connect to popular, propriety models like ChatGPT or Claude.
- Unified Interface: A single, easy-to-use interface for managing and running all your AI models.
- High Performance: leveraging Rust and Tauri for a lightweight, stylish frontend.

## Installation

### Build from Source
Parrot requires:
- Node.js (>= 16.x)
- Rust and Cargo 
- Git

1. Clone the repostory:
```
git clone https://github.com/hrszpuk/parrot.git
cd parrot
```
2. Install dependencies:
```
npm install
```
3. Build the backend:
```
npm run tauri build
```
4. Start the application:
```
npm run tauri dev
```

## Contributing
Any and all contributions are welcome!

Please read the [contribution guidelines](./CONTRIBUTING.md) for more information.
