{
  "targets": [
    {
      "target_name": "tree_sitter_toml_binding",
      "dependencies": [
        "<!(node -p \"require('node-addon-api').targets\"):node_addon_api_except",
      ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
        "src",
      ],
      "sources": [
        "src/parser.c",
        "src/scanner.c",
        "bindings/node/binding.cc",
      ],
      "cflags_c": [
        "-std=c11",
      ],
    }
  ]
}
