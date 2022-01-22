{ pkgs ? import <nixpkgs> {} }:
let
  testing-python = (pkgs.python3.withPackages (ps: with ps; [
    black
    coverage
    matplotlib
    numpy
    pytest
  ]));
in pkgs.mkShell {
  buildInputs = with pkgs; [
    testing-python
  ];

  shellHook = ''
    exec zsh
  '';
}
