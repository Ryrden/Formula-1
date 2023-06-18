{
  description = "A flake for Formula 1 Project";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:let
    forEachSystem = nixpkgs.lib.genAttrs [ "x86_64-linux" ];
  in {
    packages = forEachSystem (system: {
      default = nixpkgs.legacyPackages.${system}.callPackage ./default.nix { };
    });
  };
}
