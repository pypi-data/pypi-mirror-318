# Brunata Online API

[![License][license-shield]](LICENSE)

<!-- Sponsors -->

[![ko-fi][kofi_badge]](https://ko-fi.com/X8X3205KS)

## ⚠️ Please ensure your Brunata credentials work on [online.brunata.com][brunata] ⚠️

If your credentials don't work **AND** you use a different Brunata portal to view your metrics, please open an issue and/or merge request.

In most cases, you will likely have to add support for alternate portals yourself; I will gladly assist you in getting the authentication-flow working and finding the API endpoints. Then you can simply submit a Pull Request, and I'll review it when I have time 🙂

### ✨ Planned Features

- [x] Add support for more metrics

  - [x] 💧 Water consumption

  - [x] 🔥 District heating / gas consumption

- [ ] Configure Python tests

### The integration can fetch the following metrics

- 📊 Available meter types — ⚠️  Only tested on two accounts so far ⚠️

- ⚡ Energy meters

- 💧 Water meters

- 🔥 Heating meters — Thanks to [WallyR](https://community.home-assistant.io/u/wallyr) on the Home Assistant Community forum

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

## Credits

Active Directory B2C Login-flow was mostly based on [@itchannel](https://github.com/itchannel)'s [FordPass Integration][fordpass]

---

[brunata]: https://online.brunata.com
[fordpass]: https://github.com/itchannel/fordpass-ha
[kofi_badge]: https://ko-fi.com/img/githubbutton_sm.svg
[license-shield]: https://img.shields.io/github/license/YukiElectronics/ha-brunata.svg?style=for-the-badge
