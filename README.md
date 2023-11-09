# pythoneda-sandbox/python-artifact

Artifact space for <https://github.com/pythoneda-sandbox/python>

## How to declare it in your flake

Check the latest tag of the artifact repository: [https://github.com/pythoneda-sandbox/python-artifact-artifact/tags](https://github.com/pythoneda-sandbox/python-artifact-artifact/tags) and use it instead of the `[version]` placeholder below.

```nix
{
  description = "[..]";
  inputs = rec {
    [..]
    pythoneda-sandbox-python-artifact = {
      [optional follows]
      url =
        "github:pythoneda-sandbox/python-artifact-artifact/[version]?dir=python-artifact";
    };
  };
  outputs = [..]
};
```

Should you use another PythonEDA modules, you might want to pin those also used by this project. The same applies to [nixpkgs](https://github.com/nixos/nixpkgs "nixpkgs") and [flake-utils](https://github.com/numtide/flake-utils "flake-utils").

Use the specific package depending on your system (one of `flake-utils.lib.defaultSystems`) and Python version:

- `#packages.[system].pythoneda-sandbox-python-artifact-python38` 
- `#packages.[system].pythoneda-sandbox-python-artifact-python39` 
- `#packages.[system].pythoneda-sandbox-python-artifact-python310` 
- `#packages.[system].pythoneda-sandbox-python-artifact-python311` 

The Nix flake is under the 
[infrastructure](https://github.com/pythoneda-sandbox/python-artifact-artifact/tree/main/python-artifact "python-artifact") folder in <https://github.com/pythoneda-sandbox/python-artifact-artifact>.

