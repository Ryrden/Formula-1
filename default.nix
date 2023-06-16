{ python3Packages, ...}: python3Packages.buildPythonPackage {
  pname = "proj_labbd";
  version = "0.1.0";
  src = ./.;
  propagatedBuildInputs = with python3Packages; [
    flask
    psycopg2
  ];
}
