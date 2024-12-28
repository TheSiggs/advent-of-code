{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  # Specify dependencies for the shell
  buildInputs = with pkgs; [
    python311
  ];

  shellHook = ''
    if [ ! -d ".venv" ]; then
      python -m venv .venv
      echo "Created virtual environment in .venv"
    fi

    source .venv/bin/activate

    exec zsh
  '';
}


