# Install

## [AUR](https://aur.archlinux.org/packages/autotools-language-server)

```sh
paru -S autotools-language-server
```

## [NUR](https://nur.nix-community.org/repos/Freed-Wu)

```nix
{ config, pkgs, ... }:
{
  nixpkgs.config.packageOverrides = pkgs: {
    nur = import
      (
        builtins.fetchTarball
          "https://github.com/nix-community/NUR/archive/master.tar.gz"
      )
      {
        inherit pkgs;
      };
  };
  environment.systemPackages = with pkgs;
      (
        python3.withPackages (
          p: with p; [
            nur.repos.Freed-Wu.autotools-language-server
          ]
        )
      )
}
```

## [Nix](https://nixos.org)

```sh
nix shell github:Freed-Wu/autotools-language-server
```

Run without installation:

```sh
nix run github:Freed-Wu/autotools-language-server -- --help
```

## [PYPI](https://pypi.org/project/autotools-language-server)

```sh
pip install autotools-language-server
```

See [requirements](requirements) to know `extra_requires`.
