{ pkgs }: {
  deps = [
    pkgs.notmuch-bower
    pkgs.wget
    pkgs.docker-client
    pkgs.docker
  ];
}