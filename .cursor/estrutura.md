neoflowoff-nodemello.run/
│
├── package.json
├── .env.example
├── README.md
│
├── src/
│   ├── server.js
│   ├── config/
│   │    ├── meta.config.js
│   │    ├── twitter.config.js
│   │    ├── linkedin.config.js
│   │    ├── farcaster.config.js
│   │    ├── ipfs.config.js
│   │    └── profiles.json
│   │
│   ├── mcp/
│   │    ├── core/
│   │    │    ├── classify.js
│   │    │    ├── reduce.js
│   │    │    └── route.js
│   │    ├── visual/
│   │    │    ├── observer.js
│   │    │    ├── generators/
│   │    │    │     ├── thesis.gen.js
│   │    │    │     ├── visual.gen.js
│   │    │    │     ├── feed.gen.js
│   │    │    │     ├── story.gen.js
│   │    │    │     └── log.gen.js
│   │    │    └── reducers/
│   │    │           └── visual.reduce.js
│   │
│   ├── engine/
│   │    ├── render.js
│   │    ├── buildImage.js
│   │    └── buildVideo.js
│   │
│   ├── upload/
│   │    ├── ipfsUpload.js
│   │    └── pinataUpload.js
│   │
│   ├── distributor/
│   │    ├── instagram.js
│   │    ├── twitter.js
│   │    ├── linkedin.js
│   │    ├── farcaster.js
│   │    ├── blog.js
│   │    └── router.js
│   │
│   ├── routes/
│   │    ├── input.js
│   │    ├── render.js
│   │    ├── upload.js
│   │    └── post.js
│   │
│   └── utils/
│        ├── logger.js
│        ├── date.js
│        └── sanitize.js
│
└── fly.toml