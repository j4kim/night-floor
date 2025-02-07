# Night Floor

Système à détection de mouvement pour allumer une lumière en dessous d'une table de chevet.

## Matériel

- Microcontrôleur [Seeed Studio XIAO RP2350](https://wiki.seeedstudio.com/getting-started-xiao-rp2350/#hardware-overview)
- 2 x Capteur de mouvement [PIR HC-SR501](https://www.bastelgarage.ch/module-de-capteur-de-mouvement-pir-hc-sr501)
- 2 x Photorésistance (LDR) [GM5516](https://www.bastelgarage.ch/capteur-de-lumiere-photoresistance-gm5516)
- 2 x [Neopixel Rond 7x WS2812 RGB LED](https://www.bastelgarage.ch/neopixel-rond-7x-ws2812-rgb-led)
- 4 x Interrupteur [MTS-102](https://www.bastelgarage.ch/interrupteur-a-bascule-on-on-mts-102)

## Diagramme

```
                                                          
 ┌────────(R1MΩ)────────┐                                 
 │                      │                                 
 ├────(LDR GM5516)──┐   │                                 
 │                  │   │                                 
 │         ┌───┐    │   │                     ┌─────────┐ 
 │       ┌─│   │─┐  │   │                     │         │ 
 └─────26┼ └───┘ ┼5V┴───┴─────────────────────┼         │ 
         ┼       ┼GND───────────┐             │         │ 
         ┼       ┼              │      ┌──────┼   PIR   │ 
         ┼       ┼3─────────────┼──────┘      │         │ 
         ┼       ┼              └─────────────┼         │ 
         ┼       ┼                            │         │ 
         ┼       ┼                            └─────────┘ 
         └───────┘                                        
                                                          
```

[ASCIIFlow](https://asciiflow.com/#/share/eJyrVspLzE1VssorzcnRUcpJrEwtUrJSqo5RKkstKs7Mz4tRsjLSiVGqANKW5hZAViVIxMIEyCpJrSgBcmKUHk3peTSlASvSCDL0PbdSE5f0oykTFAiAmJi8R1OasMvhlEDTPgfFST4uQQruvqamhmaayK4g1jAsqiCCpBuAGnATCBuFJ6QhRqBYAFMNNRFmCSErkN3XBDZwCppFRmaPpuxRQBWfAeTvMQ17NGULkuAWvK4lBu1BcwyCtwfBcvdzIcIo1KSG6U%2BsRuMIHBwRAVIe4BmE30hj4j2PTXAGRe5Hj0oKQ14BDyDLhaS5dwaKobjUzsBnBRKIUapVqgUAGu8BiA%3D%3D)
