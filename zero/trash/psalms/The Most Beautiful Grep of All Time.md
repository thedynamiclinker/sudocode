The most beautiful grep of all time.

Shows everywhere in the python ecosystem where hard-coded version ranges fuck things up, despite frequent claims that doing so is somehow a "best practice."

```sh
git clone https://github.com/NixOS/nixpkgs
cd nixpkgs
grep -r -C10 'substituteInPlace' pkgs/development/python-modules/ | grep -C10 '[<>]' | grep -C10 '.*([<>]|--replace|substituteInPlace).*'
```

```
pkgs/development/python-modules/graphql-relay/default.nix-    hash = "sha256-H/HFEpg1bkgaC+AJzN/ySYMs5T8wVZwTOPIqDg0XJQw=";
pkgs/development/python-modules/graphql-relay/default.nix-  };
pkgs/development/python-modules/graphql-relay/default.nix-
pkgs/development/python-modules/graphql-relay/default.nix-  # This project doesn't seem to actually need setuptools. To find out why it
pkgs/development/python-modules/graphql-relay/default.nix-  # specifies it, follow up in:
pkgs/development/python-modules/graphql-relay/default.nix-  #
pkgs/development/python-modules/graphql-relay/default.nix-  #   https://github.com/graphql-python/graphql-relay-py/issues/49
pkgs/development/python-modules/graphql-relay/default.nix-  #
pkgs/development/python-modules/graphql-relay/default.nix-  postPatch = ''
pkgs/development/python-modules/graphql-relay/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/graphql-relay/default.nix-      --replace-fail "poetry_core>=1,<2" "poetry-core" \
pkgs/development/python-modules/graphql-relay/default.nix-      --replace ', "setuptools>=59,<70"' ""
pkgs/development/python-modules/graphql-relay/default.nix-  '';
pkgs/development/python-modules/graphql-relay/default.nix-
pkgs/development/python-modules/graphql-relay/default.nix-  nativeBuildInputs = [ poetry-core ];
pkgs/development/python-modules/graphql-relay/default.nix-
pkgs/development/python-modules/graphql-relay/default.nix-  propagatedBuildInputs = [ graphql-core ] ++ lib.optionals (pythonOlder "3.8") [ typing-extensions ];
pkgs/development/python-modules/graphql-relay/default.nix-
pkgs/development/python-modules/graphql-relay/default.nix-  nativeCheckInputs = [
pkgs/development/python-modules/graphql-relay/default.nix-    pytest-asyncio
--
pkgs/development/python-modules/aetcd/default.nix-  disabled = pythonOlder "3.8";
--
pkgs/development/python-modules/dj-rest-auth/default.nix-    # See https://github.com/iMerica/dj-rest-auth/pull/681
pkgs/development/python-modules/dj-rest-auth/default.nix-    (fetchpatch {
pkgs/development/python-modules/dj-rest-auth/default.nix-      name = "django-allauth_65.4_compatibility.patch";
pkgs/development/python-modules/dj-rest-auth/default.nix-      url = "https://github.com/iMerica/dj-rest-auth/commit/59b8cab7e2f4e3f2fdc11ab3b027a32cad45deef.patch";
pkgs/development/python-modules/dj-rest-auth/default.nix-      hash = "sha256-CH85vB3EOQvFxx+ZP2LYI4LEvaZ+ccLdXZGuAvEfStc=";
pkgs/development/python-modules/dj-rest-auth/default.nix-    })
pkgs/development/python-modules/dj-rest-auth/default.nix-  ];
pkgs/development/python-modules/dj-rest-auth/default.nix-
pkgs/development/python-modules/dj-rest-auth/default.nix-  postPatch = ''
pkgs/development/python-modules/dj-rest-auth/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/dj-rest-auth/default.nix-      --replace-fail "==" ">="
pkgs/development/python-modules/dj-rest-auth/default.nix-  '';
pkgs/development/python-modules/dj-rest-auth/default.nix-
pkgs/development/python-modules/dj-rest-auth/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/dj-rest-auth/default.nix-
pkgs/development/python-modules/dj-rest-auth/default.nix-  buildInputs = [ django ];
pkgs/development/python-modules/dj-rest-auth/default.nix-
pkgs/development/python-modules/dj-rest-auth/default.nix-  dependencies = [ djangorestframework ];
pkgs/development/python-modules/dj-rest-auth/default.nix-
pkgs/development/python-modules/dj-rest-auth/default.nix-  optional-dependencies.with_social = [
--
--
pkgs/development/python-modules/xnd/default.nix-        'include_dirs = ["${libndtypes}/include", "${ndtypes}/include", "${libxnd}/include"]' \
pkgs/development/python-modules/xnd/default.nix-      --replace-fail \
pkgs/development/python-modules/xnd/default.nix-        'library_dirs = ["libxnd", "ndtypes/libndtypes"] + LIBS' \
pkgs/development/python-modules/xnd/default.nix-        'library_dirs = ["${libndtypes}/lib", "${libxnd}/lib"]' \
pkgs/development/python-modules/xnd/default.nix-      --replace-fail \
pkgs/development/python-modules/xnd/default.nix-        'runtime_library_dirs = ["$ORIGIN"]' \
pkgs/development/python-modules/xnd/default.nix-        'runtime_library_dirs = ["${libndtypes}/lib", "${libxnd}/lib"]'
pkgs/development/python-modules/xnd/default.nix-  ''
pkgs/development/python-modules/xnd/default.nix-  + lib.optionalString (pythonAtLeast "3.12") ''
pkgs/development/python-modules/xnd/default.nix:    substituteInPlace python/xnd/util.h \
pkgs/development/python-modules/xnd/default.nix-      --replace-fail '->ob_digit[i]' '->long_value.ob_digit[i]'
pkgs/development/python-modules/xnd/default.nix-  '';
pkgs/development/python-modules/xnd/default.nix-
pkgs/development/python-modules/xnd/default.nix-  postInstall = ''
pkgs/development/python-modules/xnd/default.nix-    mkdir $out/include
pkgs/development/python-modules/xnd/default.nix-    cp python/xnd/*.h $out/include
pkgs/development/python-modules/xnd/default.nix-  ''
pkgs/development/python-modules/xnd/default.nix-  + lib.optionalString stdenv.hostPlatform.isDarwin ''
pkgs/development/python-modules/xnd/default.nix-    install_name_tool -add_rpath ${libxnd}/lib $out/${python.sitePackages}/xnd/_xnd.*.so
pkgs/development/python-modules/xnd/default.nix-  '';
--
--
pkgs/development/python-modules/amqtt/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/amqtt/default.nix-    owner = "Yakifo";
pkgs/development/python-modules/amqtt/default.nix-    repo = "amqtt";
pkgs/development/python-modules/amqtt/default.nix-    rev = "09ac98d39a711dcff0d8f22686916e1c2495144b";
pkgs/development/python-modules/amqtt/default.nix-    hash = "sha256-8T1XhBSOiArlUQbQ41LsUogDgOurLhf+M8mjIrrAC4s=";
pkgs/development/python-modules/amqtt/default.nix-  };
pkgs/development/python-modules/amqtt/default.nix-
pkgs/development/python-modules/amqtt/default.nix-  postPatch = ''
pkgs/development/python-modules/amqtt/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/amqtt/default.nix-      --replace 'transitions = "^0.8.0"' 'transitions = "*"' \
pkgs/development/python-modules/amqtt/default.nix-      --replace 'websockets = ">=9.0,<11.0"' 'websockets = "*"'
pkgs/development/python-modules/amqtt/default.nix-  '';
pkgs/development/python-modules/amqtt/default.nix-
pkgs/development/python-modules/amqtt/default.nix-  nativeBuildInputs = [ poetry-core ];
pkgs/development/python-modules/amqtt/default.nix-
pkgs/development/python-modules/amqtt/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/amqtt/default.nix-    docopt
pkgs/development/python-modules/amqtt/default.nix-    passlib
pkgs/development/python-modules/amqtt/default.nix-    pyyaml
--
pkgs/development/python-modules/sip/4.x.nix-
--
pkgs/development/python-modules/aiooui/default.nix-    repo = "aiooui";
pkgs/development/python-modules/aiooui/default.nix-    tag = "v${version}";
pkgs/development/python-modules/aiooui/default.nix-    hash = "sha256-tY8/hb3BpxzKM/IB7anfmqGcXK6FmiuoJVxqpFW1Maw=";
pkgs/development/python-modules/aiooui/default.nix-  };
pkgs/development/python-modules/aiooui/default.nix-
pkgs/development/python-modules/aiooui/default.nix-  postPatch = ''
pkgs/development/python-modules/aiooui/default.nix-    # Remove requirements and build part for the OUI data
pkgs/development/python-modules/aiooui/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/aiooui/default.nix-      --replace-fail 'script = "build_oui.py"' "" \
pkgs/development/python-modules/aiooui/default.nix-      --replace-fail ", 'requests', 'aiohttp'" "" \
pkgs/development/python-modules/aiooui/default.nix-      --replace-fail '"setuptools>=65.4.1", ' ""
pkgs/development/python-modules/aiooui/default.nix-  '';
pkgs/development/python-modules/aiooui/default.nix-
pkgs/development/python-modules/aiooui/default.nix-  build-system = [ poetry-core ];
pkgs/development/python-modules/aiooui/default.nix-
pkgs/development/python-modules/aiooui/default.nix-  nativeCheckInputs = [
pkgs/development/python-modules/aiooui/default.nix-    pytest-asyncio
pkgs/development/python-modules/aiooui/default.nix-    pytest-cov-stub
--
pkgs/development/python-modules/torchsnapshot/default.nix-    owner = "pytorch";
pkgs/development/python-modules/torchsnapshot/default.nix-    repo = "torchsnapshot";
--
pkgs/development/python-modules/vg/default.nix-
pkgs/development/python-modules/vg/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/vg/default.nix-    owner = "lace";
pkgs/development/python-modules/vg/default.nix-    repo = "vg";
pkgs/development/python-modules/vg/default.nix-    tag = version;
pkgs/development/python-modules/vg/default.nix-    hash = "sha256-ZNUAfkhjmsxD8cH0fR8Htjs+/F/3R9xfe1XgRyndids=";
pkgs/development/python-modules/vg/default.nix-  };
pkgs/development/python-modules/vg/default.nix-
pkgs/development/python-modules/vg/default.nix-  postPatch = ''
pkgs/development/python-modules/vg/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/vg/default.nix-      --replace 'requires = ["setuptools", "poetry-core>=1.0.0"]' 'requires = ["poetry-core>=1.0.0"]'
pkgs/development/python-modules/vg/default.nix-  '';
pkgs/development/python-modules/vg/default.nix-
pkgs/development/python-modules/vg/default.nix-  build-system = [ poetry-core ];
pkgs/development/python-modules/vg/default.nix-
pkgs/development/python-modules/vg/default.nix-  dependencies = [ numpy ];
pkgs/development/python-modules/vg/default.nix-
pkgs/development/python-modules/vg/default.nix-  nativeCheckInputs = [ pytestCheckHook ];
pkgs/development/python-modules/vg/default.nix-
pkgs/development/python-modules/vg/default.nix-  disabledTests = [ "test_basic" ];
--
--
pkgs/development/python-modules/numdifftools/default.nix-  ];
pkgs/development/python-modules/numdifftools/default.nix-
pkgs/development/python-modules/numdifftools/default.nix-  # Tests requires algopy and other modules which are optional and/or not available
pkgs/development/python-modules/numdifftools/default.nix-  doCheck = false;
pkgs/development/python-modules/numdifftools/default.nix-
pkgs/development/python-modules/numdifftools/default.nix-  postPatch = ''
pkgs/development/python-modules/numdifftools/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/numdifftools/default.nix-      --replace '"pytest-runner"' ""
pkgs/development/python-modules/numdifftools/default.nix-    # Remove optional dependencies
pkgs/development/python-modules/numdifftools/default.nix:    substituteInPlace requirements.txt \
pkgs/development/python-modules/numdifftools/default.nix-      --replace "algopy>=0.4" "" \
pkgs/development/python-modules/numdifftools/default.nix-      --replace "statsmodels>=0.6" ""
pkgs/development/python-modules/numdifftools/default.nix-  '';
pkgs/development/python-modules/numdifftools/default.nix-
pkgs/development/python-modules/numdifftools/default.nix-  pythonImportsCheck = [ "numdifftools" ];
pkgs/development/python-modules/numdifftools/default.nix-
pkgs/development/python-modules/numdifftools/default.nix-  meta = with lib; {
pkgs/development/python-modules/numdifftools/default.nix-    description = "Library to solve automatic numerical differentiation problems in one or more variables";
pkgs/development/python-modules/numdifftools/default.nix-    homepage = "https://github.com/pbrod/numdifftools";
pkgs/development/python-modules/numdifftools/default.nix-    license = licenses.bsd3;
--
pkgs/development/python-modules/pychromecast/default.nix-  disabled = pythonOlder "3.11";
pkgs/development/python-modules/pychromecast/default.nix-
pkgs/development/python-modules/pychromecast/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/pychromecast/default.nix-    owner = "home-assistant-libs";
pkgs/development/python-modules/pychromecast/default.nix-    repo = "pychromecast";
pkgs/development/python-modules/pychromecast/default.nix-    tag = version;
pkgs/development/python-modules/pychromecast/default.nix-    hash = "sha256-NB/KXKgmyLAhsL/CD463eNMO8brye5LKVCkkD3EloPU=";
pkgs/development/python-modules/pychromecast/default.nix-  };
pkgs/development/python-modules/pychromecast/default.nix-
pkgs/development/python-modules/pychromecast/default.nix-  postPatch = ''
pkgs/development/python-modules/pychromecast/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/pychromecast/default.nix-       --replace-fail "setuptools>=65.6,<78.0" setuptools \
pkgs/development/python-modules/pychromecast/default.nix-       --replace-fail "wheel>=0.37.1,<0.46.0" wheel
pkgs/development/python-modules/pychromecast/default.nix-  '';
pkgs/development/python-modules/pychromecast/default.nix-
pkgs/development/python-modules/pychromecast/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/pychromecast/default.nix-
pkgs/development/python-modules/pychromecast/default.nix-  dependencies = [
pkgs/development/python-modules/pychromecast/default.nix-    casttube
pkgs/development/python-modules/pychromecast/default.nix-    protobuf
pkgs/development/python-modules/pychromecast/default.nix-    zeroconf
--
pkgs/development/python-modules/robotstatuschecker/default.nix-  # no tests included in PyPI tarball
--
pkgs/development/python-modules/gremlinpython/default.nix-    tag = version;
pkgs/development/python-modules/gremlinpython/default.nix-    hash = "sha256-Yc0l3kE+6dM9v4QUZPFpm/yjDCrqVO35Vy5srEjAExE=";
pkgs/development/python-modules/gremlinpython/default.nix-  };
pkgs/development/python-modules/gremlinpython/default.nix-
pkgs/development/python-modules/gremlinpython/default.nix-  sourceRoot = "${src.name}/gremlin-python/src/main/python";
pkgs/development/python-modules/gremlinpython/default.nix-
pkgs/development/python-modules/gremlinpython/default.nix-  postPatch = ''
pkgs/development/python-modules/gremlinpython/default.nix-    sed -i '/pytest-runner/d' setup.py
pkgs/development/python-modules/gremlinpython/default.nix-
pkgs/development/python-modules/gremlinpython/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/gremlinpython/default.nix-      --replace 'importlib-metadata<5.0.0' 'importlib-metadata' \
pkgs/development/python-modules/gremlinpython/default.nix-      --replace "os.getenv('VERSION', '?').replace('-SNAPSHOT', '.dev-%d' % timestamp)" '"${version}"'
pkgs/development/python-modules/gremlinpython/default.nix-  '';
pkgs/development/python-modules/gremlinpython/default.nix-
pkgs/development/python-modules/gremlinpython/default.nix-  # setup-requires requirements
pkgs/development/python-modules/gremlinpython/default.nix-  nativeBuildInputs = [ importlib-metadata ];
pkgs/development/python-modules/gremlinpython/default.nix-
pkgs/development/python-modules/gremlinpython/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/gremlinpython/default.nix-    aenum
pkgs/development/python-modules/gremlinpython/default.nix-    aiohttp
--
--
pkgs/development/python-modules/grpcio-status/default.nix-  disabled = pythonOlder "3.6";
pkgs/development/python-modules/grpcio-status/default.nix-
pkgs/development/python-modules/grpcio-status/default.nix-  src = fetchPypi {
pkgs/development/python-modules/grpcio-status/default.nix-    pname = "grpcio_status";
pkgs/development/python-modules/grpcio-status/default.nix-    inherit version;
pkgs/development/python-modules/grpcio-status/default.nix-    hash = "sha256-xYwbJKpFTjDx/Gp+DbvBlMVKQIFDlxqUtfTkC7WDFDI=";
pkgs/development/python-modules/grpcio-status/default.nix-  };
pkgs/development/python-modules/grpcio-status/default.nix-
pkgs/development/python-modules/grpcio-status/default.nix-  postPatch = ''
pkgs/development/python-modules/grpcio-status/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/grpcio-status/default.nix-      --replace 'protobuf>=4.21.6' 'protobuf'
pkgs/development/python-modules/grpcio-status/default.nix-  '';
pkgs/development/python-modules/grpcio-status/default.nix-
pkgs/development/python-modules/grpcio-status/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/grpcio-status/default.nix-    googleapis-common-protos
pkgs/development/python-modules/grpcio-status/default.nix-    grpcio
pkgs/development/python-modules/grpcio-status/default.nix-    protobuf
pkgs/development/python-modules/grpcio-status/default.nix-  ];
pkgs/development/python-modules/grpcio-status/default.nix-
pkgs/development/python-modules/grpcio-status/default.nix-  # Project thas no tests
--
--
pkgs/development/python-modules/pyhocon/default.nix-    python-dateutil
pkgs/development/python-modules/pyhocon/default.nix-  ];
pkgs/development/python-modules/pyhocon/default.nix-
pkgs/development/python-modules/pyhocon/default.nix-  nativeCheckInputs = [
pkgs/development/python-modules/pyhocon/default.nix-    mock
pkgs/development/python-modules/pyhocon/default.nix-    pytestCheckHook
pkgs/development/python-modules/pyhocon/default.nix-  ];
pkgs/development/python-modules/pyhocon/default.nix-
pkgs/development/python-modules/pyhocon/default.nix-  postPatch = ''
pkgs/development/python-modules/pyhocon/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/pyhocon/default.nix-      --replace "pyparsing~=2.0" "pyparsing>=2.0"
pkgs/development/python-modules/pyhocon/default.nix-  '';
pkgs/development/python-modules/pyhocon/default.nix-
pkgs/development/python-modules/pyhocon/default.nix-  pythonImportsCheck = [ "pyhocon" ];
pkgs/development/python-modules/pyhocon/default.nix-
pkgs/development/python-modules/pyhocon/default.nix-  disabledTestPaths = [
pkgs/development/python-modules/pyhocon/default.nix-    # pyparsing.exceptions.ParseException: Expected end of text, found '='
pkgs/development/python-modules/pyhocon/default.nix-    # https://github.com/chimpler/pyhocon/issues/273
pkgs/development/python-modules/pyhocon/default.nix-    "tests/test_tool.py"
pkgs/development/python-modules/pyhocon/default.nix-  ];
--
--
pkgs/development/python-modules/scikit-learn/default.nix-    pname = "scikit_learn";
pkgs/development/python-modules/scikit-learn/default.nix-    inherit version;
pkgs/development/python-modules/scikit-learn/default.nix-    hash = "sha256-JLPx6XakZlqnTuD8qsK4/Mxq53yOB6sl2jum0ykrmAI=";
pkgs/development/python-modules/scikit-learn/default.nix-  };
pkgs/development/python-modules/scikit-learn/default.nix-
pkgs/development/python-modules/scikit-learn/default.nix-  postPatch = ''
pkgs/development/python-modules/scikit-learn/default.nix:    substituteInPlace meson.build --replace-fail \
pkgs/development/python-modules/scikit-learn/default.nix-      "run_command('sklearn/_build_utils/version.py', check: true).stdout().strip()," \
pkgs/development/python-modules/scikit-learn/default.nix-      "'${version}',"
pkgs/development/python-modules/scikit-learn/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/scikit-learn/default.nix-      --replace-fail "numpy>=2,<2.3.0" numpy \
pkgs/development/python-modules/scikit-learn/default.nix-      --replace-fail "scipy>=1.8.0,<1.16.0" scipy
pkgs/development/python-modules/scikit-learn/default.nix-  '';
pkgs/development/python-modules/scikit-learn/default.nix-
pkgs/development/python-modules/scikit-learn/default.nix-  buildInputs = [
pkgs/development/python-modules/scikit-learn/default.nix-    numpy.blas
pkgs/development/python-modules/scikit-learn/default.nix-    pillow
pkgs/development/python-modules/scikit-learn/default.nix-    glibcLocales
pkgs/development/python-modules/scikit-learn/default.nix-  ]
pkgs/development/python-modules/scikit-learn/default.nix-  ++ lib.optionals stdenv.cc.isClang [ llvmPackages.openmp ];
--
pkgs/development/python-modules/python-etcd/default.nix-    etcd_3_4
pkgs/development/python-modules/python-etcd/default.nix-    mock
pkgs/development/python-modules/python-etcd/default.nix-    pyopenssl
pkgs/development/python-modules/python-etcd/default.nix-  ];
pkgs/development/python-modules/python-etcd/default.nix-
pkgs/development/python-modules/python-etcd/default.nix-  # arm64 is an unsupported platform on etcd 3.4. should be able to be removed on >= etcd 3.5
pkgs/development/python-modules/python-etcd/default.nix-  doCheck = !stdenv.hostPlatform.isAarch64;
pkgs/development/python-modules/python-etcd/default.nix-
pkgs/development/python-modules/python-etcd/default.nix-  preCheck = ''
pkgs/development/python-modules/python-etcd/default.nix-    for file in "test_auth" "integration/test_simple"; do
pkgs/development/python-modules/python-etcd/default.nix:      substituteInPlace src/etcd/tests/$file.py \
pkgs/development/python-modules/python-etcd/default.nix-        --replace-fail "assertEquals" "assertEqual"
pkgs/development/python-modules/python-etcd/default.nix-    done
pkgs/development/python-modules/python-etcd/default.nix-  '';
pkgs/development/python-modules/python-etcd/default.nix-
pkgs/development/python-modules/python-etcd/default.nix-  disabledTests = lib.optionals stdenv.hostPlatform.isDarwin [
pkgs/development/python-modules/python-etcd/default.nix-    # Seems to be failing because of network restrictions
pkgs/development/python-modules/python-etcd/default.nix-    # AttributeError: Can't get local object 'TestWatch.test_watch_indexed_generator.<locals>.watch_value'
pkgs/development/python-modules/python-etcd/default.nix-    "test_watch"
pkgs/development/python-modules/python-etcd/default.nix-    "test_watch_generator"
pkgs/development/python-modules/python-etcd/default.nix-    "test_watch_indexed"
--
pkgs/development/python-modules/cvelib/default.nix-
pkgs/development/python-modules/cvelib/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/cvelib/default.nix-    owner = "RedHatProductSecurity";
pkgs/development/python-modules/cvelib/default.nix-    repo = "cvelib";
pkgs/development/python-modules/cvelib/default.nix-    tag = version;
pkgs/development/python-modules/cvelib/default.nix-    hash = "sha256-AhA+2lEI/hsbIVCfSWO0vI6eWkObjsq5xYOSqVvUPkU=";
--
pkgs/development/python-modules/bitcoin-utils-fork-minimal/default.nix-  };
pkgs/development/python-modules/bitcoin-utils-fork-minimal/default.nix-
pkgs/development/python-modules/bitcoin-utils-fork-minimal/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/bitcoin-utils-fork-minimal/default.nix-    base58
pkgs/development/python-modules/bitcoin-utils-fork-minimal/default.nix-    ecdsa
pkgs/development/python-modules/bitcoin-utils-fork-minimal/default.nix-    sympy
pkgs/development/python-modules/bitcoin-utils-fork-minimal/default.nix-  ];
pkgs/development/python-modules/bitcoin-utils-fork-minimal/default.nix-
pkgs/development/python-modules/bitcoin-utils-fork-minimal/default.nix-  preConfigure = ''
pkgs/development/python-modules/bitcoin-utils-fork-minimal/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/bitcoin-utils-fork-minimal/default.nix-      --replace "sympy==1.3" "sympy>=1.3" \
pkgs/development/python-modules/bitcoin-utils-fork-minimal/default.nix-      --replace "base58==2.1.0" "base58>=2.1.0" \
pkgs/development/python-modules/bitcoin-utils-fork-minimal/default.nix-      --replace "ecdsa==0.17.0" "ecdsa>=0.17.0"
pkgs/development/python-modules/bitcoin-utils-fork-minimal/default.nix-  '';
pkgs/development/python-modules/bitcoin-utils-fork-minimal/default.nix-
pkgs/development/python-modules/bitcoin-utils-fork-minimal/default.nix-  # Project doesn't ship tests
pkgs/development/python-modules/bitcoin-utils-fork-minimal/default.nix-  doCheck = false;
pkgs/development/python-modules/bitcoin-utils-fork-minimal/default.nix-
pkgs/development/python-modules/bitcoin-utils-fork-minimal/default.nix-  pythonImportsCheck = [ "bitcoinutils" ];
pkgs/development/python-modules/bitcoin-utils-fork-minimal/default.nix-
--
pkgs/development/python-modules/django-filingcabinet/default.nix-    repo = "django-filingcabinet";
pkgs/development/python-modules/django-filingcabinet/default.nix-    # No release tagged yet on GitHub
--
pkgs/development/python-modules/ledgerwallet/default.nix-    intelhex
pkgs/development/python-modules/ledgerwallet/default.nix-    pillow
pkgs/development/python-modules/ledgerwallet/default.nix-    protobuf
pkgs/development/python-modules/ledgerwallet/default.nix-    requests
pkgs/development/python-modules/ledgerwallet/default.nix-    tabulate
pkgs/development/python-modules/ledgerwallet/default.nix-    toml
pkgs/development/python-modules/ledgerwallet/default.nix-  ];
pkgs/development/python-modules/ledgerwallet/default.nix-
pkgs/development/python-modules/ledgerwallet/default.nix-  postPatch = ''
pkgs/development/python-modules/ledgerwallet/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/ledgerwallet/default.nix-      --replace-fail '"protobuf >=3.20,<4"' '"protobuf >=3.20"'
pkgs/development/python-modules/ledgerwallet/default.nix-  '';
pkgs/development/python-modules/ledgerwallet/default.nix-
pkgs/development/python-modules/ledgerwallet/default.nix-  # Regenerate protobuf bindings to lift the version upper-bound and enable
pkgs/development/python-modules/ledgerwallet/default.nix-  # compatibility the current default protobuf library.
pkgs/development/python-modules/ledgerwallet/default.nix-  preBuild = ''
pkgs/development/python-modules/ledgerwallet/default.nix-    protoc --python_out=. --pyi_out=. ledgerwallet/proto/*.proto
pkgs/development/python-modules/ledgerwallet/default.nix-  '';
pkgs/development/python-modules/ledgerwallet/default.nix-
pkgs/development/python-modules/ledgerwallet/default.nix-  pythonImportsCheck = [ "ledgerwallet" ];
--
--
pkgs/development/python-modules/pymssql/default.nix-  version = "2.3.7";
pkgs/development/python-modules/pymssql/default.nix-  pyproject = true;
pkgs/development/python-modules/pymssql/default.nix-
pkgs/development/python-modules/pymssql/default.nix-  src = fetchPypi {
pkgs/development/python-modules/pymssql/default.nix-    inherit pname version;
pkgs/development/python-modules/pymssql/default.nix-    hash = "sha256-Xm15x7HOxArr7EsJnG5EXMqsJFGeXnZ7SaTm9IwIflA=";
pkgs/development/python-modules/pymssql/default.nix-  };
pkgs/development/python-modules/pymssql/default.nix-
pkgs/development/python-modules/pymssql/default.nix-  postPatch = ''
pkgs/development/python-modules/pymssql/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/pymssql/default.nix-      --replace-fail "setuptools>=54.0,<70.3" "setuptools>=54.0"
pkgs/development/python-modules/pymssql/default.nix-  '';
pkgs/development/python-modules/pymssql/default.nix-
pkgs/development/python-modules/pymssql/default.nix-  build-system = [
pkgs/development/python-modules/pymssql/default.nix-    cython
pkgs/development/python-modules/pymssql/default.nix-    setuptools-scm
pkgs/development/python-modules/pymssql/default.nix-    tomli
pkgs/development/python-modules/pymssql/default.nix-  ];
pkgs/development/python-modules/pymssql/default.nix-
pkgs/development/python-modules/pymssql/default.nix-  buildInputs = [
--
--
pkgs/development/python-modules/universal-silabs-flasher/default.nix-
pkgs/development/python-modules/universal-silabs-flasher/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/universal-silabs-flasher/default.nix-    owner = "NabuCasa";
pkgs/development/python-modules/universal-silabs-flasher/default.nix-    repo = "universal-silabs-flasher";
pkgs/development/python-modules/universal-silabs-flasher/default.nix-    tag = "v${version}";
pkgs/development/python-modules/universal-silabs-flasher/default.nix-    hash = "sha256-AnZhs9uR0lHY8CxYlbfblnftahnbC2LgwtyDVQCYizI=";
pkgs/development/python-modules/universal-silabs-flasher/default.nix-  };
pkgs/development/python-modules/universal-silabs-flasher/default.nix-
pkgs/development/python-modules/universal-silabs-flasher/default.nix-  postPatch = ''
pkgs/development/python-modules/universal-silabs-flasher/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/universal-silabs-flasher/default.nix-      --replace-fail '"setuptools-git-versioning>=2.0,<3"' "" \
pkgs/development/python-modules/universal-silabs-flasher/default.nix-      --replace-fail 'dynamic = ["version"]' 'version = "${version}"'
pkgs/development/python-modules/universal-silabs-flasher/default.nix-  '';
pkgs/development/python-modules/universal-silabs-flasher/default.nix-
pkgs/development/python-modules/universal-silabs-flasher/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/universal-silabs-flasher/default.nix-
pkgs/development/python-modules/universal-silabs-flasher/default.nix-  dependencies = [
pkgs/development/python-modules/universal-silabs-flasher/default.nix-    bellows
pkgs/development/python-modules/universal-silabs-flasher/default.nix-    click
pkgs/development/python-modules/universal-silabs-flasher/default.nix-    coloredlogs
--
--
pkgs/development/python-modules/pipdeptree/default.nix-    owner = "tox-dev";
pkgs/development/python-modules/pipdeptree/default.nix-    repo = "pipdeptree";
pkgs/development/python-modules/pipdeptree/default.nix-    tag = version;
pkgs/development/python-modules/pipdeptree/default.nix-    hash = "sha256-PYlNMAomqN9T60b8bRqb8mnLjFRn3JnI79Tynncxje8=";
pkgs/development/python-modules/pipdeptree/default.nix-  };
pkgs/development/python-modules/pipdeptree/default.nix-
pkgs/development/python-modules/pipdeptree/default.nix-  postPatch = ''
pkgs/development/python-modules/pipdeptree/default.nix-    # only set to ensure py3.13 compat
pkgs/development/python-modules/pipdeptree/default.nix-    # https://github.com/tox-dev/pipdeptree/pull/406
pkgs/development/python-modules/pipdeptree/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/pipdeptree/default.nix-      --replace-fail '"pip>=24.2"' '"pip"'
pkgs/development/python-modules/pipdeptree/default.nix-  '';
pkgs/development/python-modules/pipdeptree/default.nix-
pkgs/development/python-modules/pipdeptree/default.nix-  build-system = [
pkgs/development/python-modules/pipdeptree/default.nix-    hatchling
pkgs/development/python-modules/pipdeptree/default.nix-    hatch-vcs
pkgs/development/python-modules/pipdeptree/default.nix-  ];
pkgs/development/python-modules/pipdeptree/default.nix-
pkgs/development/python-modules/pipdeptree/default.nix-  dependencies = [
pkgs/development/python-modules/pipdeptree/default.nix-    pip
--
pkgs/development/python-modules/mmengine/default.nix-    })
pkgs/development/python-modules/mmengine/default.nix-  ];
pkgs/development/python-modules/mmengine/default.nix-
pkgs/development/python-modules/mmengine/default.nix-  postPatch =
pkgs/development/python-modules/mmengine/default.nix-    # Fails in python >= 3.13
pkgs/development/python-modules/mmengine/default.nix-    # exec(compile(f.read(), version_file, "exec")) does not populate the locals() namesp
pkgs/development/python-modules/mmengine/default.nix-    # In python 3.13, the locals() dictionary in a function does not automatically update with
pkgs/development/python-modules/mmengine/default.nix-    # changes made by exec().
pkgs/development/python-modules/mmengine/default.nix-    # https://peps.python.org/pep-0558/
pkgs/development/python-modules/mmengine/default.nix-    ''
pkgs/development/python-modules/mmengine/default.nix:      substituteInPlace setup.py \
pkgs/development/python-modules/mmengine/default.nix-        --replace-fail \
pkgs/development/python-modules/mmengine/default.nix-          "return locals()['__version__']" \
pkgs/development/python-modules/mmengine/default.nix-          "return '${version}'"
pkgs/development/python-modules/mmengine/default.nix-    ''
--
pkgs/development/python-modules/opentype-feature-freezer/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/opentype-feature-freezer/default.nix-    owner = "twardoch";
pkgs/development/python-modules/opentype-feature-freezer/default.nix-    repo = "fonttools-opentype-feature-freezer";
pkgs/development/python-modules/opentype-feature-freezer/default.nix-    rev = "2ae16853bc724c3e377726f81d9fc661d3445827";
pkgs/development/python-modules/opentype-feature-freezer/default.nix-    hash = "sha256-mIWQF9LTVKxIkwHLCTVK1cOuiaduJyX8pyBZ/0RKIVE=";
pkgs/development/python-modules/opentype-feature-freezer/default.nix-  };
pkgs/development/python-modules/opentype-feature-freezer/default.nix-
pkgs/development/python-modules/opentype-feature-freezer/default.nix-  postPatch = ''
pkgs/development/python-modules/opentype-feature-freezer/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/opentype-feature-freezer/default.nix-      --replace-fail poetry.masonry.api poetry.core.masonry.api \
pkgs/development/python-modules/opentype-feature-freezer/default.nix-      --replace-fail "poetry>=" "poetry-core>="
pkgs/development/python-modules/opentype-feature-freezer/default.nix-  '';
pkgs/development/python-modules/opentype-feature-freezer/default.nix-
pkgs/development/python-modules/opentype-feature-freezer/default.nix-  build-system = [
pkgs/development/python-modules/opentype-feature-freezer/default.nix-    poetry-core
pkgs/development/python-modules/opentype-feature-freezer/default.nix-    configparser
pkgs/development/python-modules/opentype-feature-freezer/default.nix-  ];
pkgs/development/python-modules/opentype-feature-freezer/default.nix-
pkgs/development/python-modules/opentype-feature-freezer/default.nix-  dependencies = [ fonttools ];
--
pkgs/development/python-modules/ua-parser-builtins/default.nix-
--
pkgs/development/python-modules/cltk/default.nix-
pkgs/development/python-modules/cltk/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/cltk/default.nix-    owner = "cltk";
pkgs/development/python-modules/cltk/default.nix-    repo = "cltk";
pkgs/development/python-modules/cltk/default.nix-    tag = "v${version}";
pkgs/development/python-modules/cltk/default.nix-    hash = "sha256-aeWbfDVNn6DwW+KFh62n5RBgWp5uSWDv2RHmB27/xI4=";
pkgs/development/python-modules/cltk/default.nix-  };
pkgs/development/python-modules/cltk/default.nix-
pkgs/development/python-modules/cltk/default.nix-  postPatch = ''
pkgs/development/python-modules/cltk/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/cltk/default.nix-      --replace-fail "poetry>=1.1.13" poetry-core \
pkgs/development/python-modules/cltk/default.nix-      --replace-fail "poetry.masonry.api" "poetry.core.masonry.api" \
pkgs/development/python-modules/cltk/default.nix-      --replace-fail 'scipy = "<1.13.0"' 'scipy = "^1"' \
pkgs/development/python-modules/cltk/default.nix-      --replace-fail 'boltons = "^21.0.0"' 'boltons = "^24.0.0"'
pkgs/development/python-modules/cltk/default.nix-  '';
pkgs/development/python-modules/cltk/default.nix-
pkgs/development/python-modules/cltk/default.nix-  build-system = [ poetry-core ];
pkgs/development/python-modules/cltk/default.nix-
pkgs/development/python-modules/cltk/default.nix-  pythonRelaxDeps = [
pkgs/development/python-modules/cltk/default.nix-    "spacy"
--
pkgs/development/python-modules/daltonlens/default.nix-  pname = "daltonlens";
pkgs/development/python-modules/daltonlens/default.nix-  version = "0.1.5";
--
pkgs/development/python-modules/daltonlens/default.nix-
pkgs/development/python-modules/daltonlens/default.nix-  build-system = [
pkgs/development/python-modules/daltonlens/default.nix-    setuptools
pkgs/development/python-modules/daltonlens/default.nix-  ];
pkgs/development/python-modules/daltonlens/default.nix-
pkgs/development/python-modules/daltonlens/default.nix-  dependencies = [
pkgs/development/python-modules/daltonlens/default.nix-    numpy
pkgs/development/python-modules/daltonlens/default.nix-    pillow
--
pkgs/development/python-modules/qgrid/default.nix-  patches = [
pkgs/development/python-modules/qgrid/default.nix-    # Fixes compatibility of qgrid with ipywidgets >= 8.0.0
pkgs/development/python-modules/qgrid/default.nix-    # See https://github.com/quantopian/qgrid/pull/331
pkgs/development/python-modules/qgrid/default.nix-    (fetchpatch {
pkgs/development/python-modules/qgrid/default.nix-      url = "https://github.com/quantopian/qgrid/pull/331/commits/8cc50d5117d4208a9dd672418021c59898e2d1b2.patch";
pkgs/development/python-modules/qgrid/default.nix-      hash = "sha256-+NLz4yBUGUXKyukPVE4PehenPzjnfljR5RAX7CEtpV4=";
pkgs/development/python-modules/qgrid/default.nix-    })
pkgs/development/python-modules/qgrid/default.nix-  ];
pkgs/development/python-modules/qgrid/default.nix-
pkgs/development/python-modules/qgrid/default.nix-  postPatch = ''
pkgs/development/python-modules/qgrid/default.nix:    substituteInPlace qgrid/grid.py \
pkgs/development/python-modules/qgrid/default.nix-      --replace-fail "from distutils.version import LooseVersion" "from looseversion import LooseVersion"
--
pkgs/development/python-modules/zope-testing/default.nix-
pkgs/development/python-modules/zope-testing/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/zope-testing/default.nix-    owner = "zopefoundation";
pkgs/development/python-modules/zope-testing/default.nix-    repo = "zope.testing";
pkgs/development/python-modules/zope-testing/default.nix-    tag = version;
pkgs/development/python-modules/zope-testing/default.nix-    hash = "sha256-G9RfRsXSzQ92HeBF5dRTI+1XEz1HM3DuB0ypZ61uHfw=";
pkgs/development/python-modules/zope-testing/default.nix-  };
pkgs/development/python-modules/zope-testing/default.nix-
pkgs/development/python-modules/zope-testing/default.nix-  postPatch = ''
pkgs/development/python-modules/zope-testing/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/zope-testing/default.nix-      --replace-fail "setuptools <= 75.6.0" setuptools
pkgs/development/python-modules/zope-testing/default.nix-  '';
pkgs/development/python-modules/zope-testing/default.nix-
pkgs/development/python-modules/zope-testing/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/zope-testing/default.nix-
pkgs/development/python-modules/zope-testing/default.nix-  doCheck = !isPyPy;
pkgs/development/python-modules/zope-testing/default.nix-
pkgs/development/python-modules/zope-testing/default.nix-  nativeCheckInputs = [ pytestCheckHook ];
pkgs/development/python-modules/zope-testing/default.nix-
pkgs/development/python-modules/zope-testing/default.nix-  enabledTestPaths = [ "src/zope/testing/tests.py" ];
--
--
pkgs/development/python-modules/msprime/default.nix-  disabled = pythonOlder "3.8";
pkgs/development/python-modules/msprime/default.nix-
pkgs/development/python-modules/msprime/default.nix-  src = fetchPypi {
pkgs/development/python-modules/msprime/default.nix-    inherit pname version;
pkgs/development/python-modules/msprime/default.nix-    hash = "sha256-0PlEo3pREx34zZZ5fyR5gXPEC6L/XAlFgdHKVvxRFzA=";
pkgs/development/python-modules/msprime/default.nix-  };
pkgs/development/python-modules/msprime/default.nix-
pkgs/development/python-modules/msprime/default.nix-  postPatch = ''
pkgs/development/python-modules/msprime/default.nix-    # build-time constriant, used to ensure forward and backward compat
pkgs/development/python-modules/msprime/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/msprime/default.nix-      --replace-fail "numpy>=2" "numpy"
pkgs/development/python-modules/msprime/default.nix-  '';
pkgs/development/python-modules/msprime/default.nix-
pkgs/development/python-modules/msprime/default.nix-  nativeBuildInputs = [
pkgs/development/python-modules/msprime/default.nix-    gsl
pkgs/development/python-modules/msprime/default.nix-    oldest-supported-numpy
pkgs/development/python-modules/msprime/default.nix-    setuptools-scm
pkgs/development/python-modules/msprime/default.nix-    wheel
pkgs/development/python-modules/msprime/default.nix-  ];
pkgs/development/python-modules/msprime/default.nix-
--
--
pkgs/development/python-modules/hdmedians/default.nix-    hash = "sha256-tHrssWdx4boHNlVyVdgK4CQLCRVr/0NDId5VmzWawtY=";
pkgs/development/python-modules/hdmedians/default.nix-  };
pkgs/development/python-modules/hdmedians/default.nix-
pkgs/development/python-modules/hdmedians/default.nix-  patches = [
pkgs/development/python-modules/hdmedians/default.nix-    # https://github.com/daleroberts/hdmedians/pull/10
pkgs/development/python-modules/hdmedians/default.nix-    ./replace-nose.patch
pkgs/development/python-modules/hdmedians/default.nix-  ];
pkgs/development/python-modules/hdmedians/default.nix-
pkgs/development/python-modules/hdmedians/default.nix-  postPatch = ''
pkgs/development/python-modules/hdmedians/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/hdmedians/default.nix-      --replace-fail "'nose>=1.0'," ""
pkgs/development/python-modules/hdmedians/default.nix-  '';
pkgs/development/python-modules/hdmedians/default.nix-
pkgs/development/python-modules/hdmedians/default.nix-  build-system = [
pkgs/development/python-modules/hdmedians/default.nix-    cython
pkgs/development/python-modules/hdmedians/default.nix-    oldest-supported-numpy
pkgs/development/python-modules/hdmedians/default.nix-    setuptools
pkgs/development/python-modules/hdmedians/default.nix-  ];
pkgs/development/python-modules/hdmedians/default.nix-
pkgs/development/python-modules/hdmedians/default.nix-  dependencies = [ numpy ];
--
--
pkgs/development/python-modules/scikit-misc/default.nix-    repo = "scikit-misc";
pkgs/development/python-modules/scikit-misc/default.nix-    tag = "v${version}";
pkgs/development/python-modules/scikit-misc/default.nix-    hash = "sha256-w6RHmVxJjLx9ov2LxXvicxmY8jixfkIRfbfVnV2yhOU=";
pkgs/development/python-modules/scikit-misc/default.nix-  };
pkgs/development/python-modules/scikit-misc/default.nix-
pkgs/development/python-modules/scikit-misc/default.nix-  postPatch = ''
pkgs/development/python-modules/scikit-misc/default.nix-    patchShebangs .
pkgs/development/python-modules/scikit-misc/default.nix-
pkgs/development/python-modules/scikit-misc/default.nix-    # unbound numpy and disable coverage testing in pytest
pkgs/development/python-modules/scikit-misc/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/scikit-misc/default.nix-      --replace-fail 'numpy>=2.0' 'numpy' \
pkgs/development/python-modules/scikit-misc/default.nix-      --replace-fail 'addopts = "' '#addopts = "'
pkgs/development/python-modules/scikit-misc/default.nix-
pkgs/development/python-modules/scikit-misc/default.nix-    # provide a version to use when git fails to get the tag
pkgs/development/python-modules/scikit-misc/default.nix-    [[ -f skmisc/_version.py ]] || \
pkgs/development/python-modules/scikit-misc/default.nix-      echo '__version__ = "${version}"' > skmisc/_version.py
pkgs/development/python-modules/scikit-misc/default.nix-  '';
pkgs/development/python-modules/scikit-misc/default.nix-
pkgs/development/python-modules/scikit-misc/default.nix-  nativeBuildInputs = [
pkgs/development/python-modules/scikit-misc/default.nix-    gfortran
--
pkgs/development/python-modules/cxxfilt/default.nix-  src = fetchPypi {
pkgs/development/python-modules/cxxfilt/default.nix-    inherit pname version;
pkgs/development/python-modules/cxxfilt/default.nix-    sha256 = "7df6464ba5e8efbf0d8974c0b2c78b32546676f06059a83515dbdfa559b34214";
pkgs/development/python-modules/cxxfilt/default.nix-  };
pkgs/development/python-modules/cxxfilt/default.nix-
--
pkgs/development/python-modules/luna-usb/default.nix-
pkgs/development/python-modules/luna-usb/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/luna-usb/default.nix-    owner = "greatscottgadgets";
pkgs/development/python-modules/luna-usb/default.nix-    repo = "luna";
pkgs/development/python-modules/luna-usb/default.nix-    tag = version;
pkgs/development/python-modules/luna-usb/default.nix-    hash = "sha256-gySaNbebWUS8wS8adPQo1mT+jmdb+2ddlMckTa36JCY=";
pkgs/development/python-modules/luna-usb/default.nix-  };
pkgs/development/python-modules/luna-usb/default.nix-
pkgs/development/python-modules/luna-usb/default.nix-  postPatch = ''
pkgs/development/python-modules/luna-usb/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/luna-usb/default.nix-      --replace-fail '"setuptools-git-versioning<2"' "" \
pkgs/development/python-modules/luna-usb/default.nix-      --replace-fail 'dynamic = ["version"]' 'version = "${version}"'
pkgs/development/python-modules/luna-usb/default.nix-  '';
pkgs/development/python-modules/luna-usb/default.nix-
pkgs/development/python-modules/luna-usb/default.nix-  build-system = [
pkgs/development/python-modules/luna-usb/default.nix-    setuptools
pkgs/development/python-modules/luna-usb/default.nix-  ];
pkgs/development/python-modules/luna-usb/default.nix-
pkgs/development/python-modules/luna-usb/default.nix-  dependencies = [
pkgs/development/python-modules/luna-usb/default.nix-    amaranth
--
--
pkgs/development/python-modules/ha-silabs-firmware-client/default.nix-
pkgs/development/python-modules/ha-silabs-firmware-client/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/ha-silabs-firmware-client/default.nix-    owner = "home-assistant-libs";
pkgs/development/python-modules/ha-silabs-firmware-client/default.nix-    repo = "ha-silabs-firmware-client";
pkgs/development/python-modules/ha-silabs-firmware-client/default.nix-    tag = "v${version}";
pkgs/development/python-modules/ha-silabs-firmware-client/default.nix-    hash = "sha256-Kip9JL9tuF7OI22elN0w2Z7Xjdaayboo8LThp4FAets=";
pkgs/development/python-modules/ha-silabs-firmware-client/default.nix-  };
pkgs/development/python-modules/ha-silabs-firmware-client/default.nix-
pkgs/development/python-modules/ha-silabs-firmware-client/default.nix-  postPatch = ''
pkgs/development/python-modules/ha-silabs-firmware-client/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/ha-silabs-firmware-client/default.nix-      --replace-fail ', "setuptools-git-versioning<3"' "" \
pkgs/development/python-modules/ha-silabs-firmware-client/default.nix-      --replace-fail 'dynamic = ["version"]' 'version = "${version}"'
pkgs/development/python-modules/ha-silabs-firmware-client/default.nix-  '';
pkgs/development/python-modules/ha-silabs-firmware-client/default.nix-
pkgs/development/python-modules/ha-silabs-firmware-client/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/ha-silabs-firmware-client/default.nix-
pkgs/development/python-modules/ha-silabs-firmware-client/default.nix-  dependencies = [
pkgs/development/python-modules/ha-silabs-firmware-client/default.nix-    aiohttp
pkgs/development/python-modules/ha-silabs-firmware-client/default.nix-    yarl
pkgs/development/python-modules/ha-silabs-firmware-client/default.nix-  ];
--
--
pkgs/development/python-modules/ovoenergy/default.nix-
pkgs/development/python-modules/ovoenergy/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/ovoenergy/default.nix-    owner = "timmo001";
pkgs/development/python-modules/ovoenergy/default.nix-    repo = "ovoenergy";
pkgs/development/python-modules/ovoenergy/default.nix-    tag = version;
pkgs/development/python-modules/ovoenergy/default.nix-    hash = "sha256-7SXnOyvBsBPQ+4tC6pcEXGtcLdqKjzlB2xDZmw/uWcM=";
pkgs/development/python-modules/ovoenergy/default.nix-  };
pkgs/development/python-modules/ovoenergy/default.nix-
pkgs/development/python-modules/ovoenergy/default.nix-  postPatch = ''
pkgs/development/python-modules/ovoenergy/default.nix:    substituteInPlace requirements_setup.txt \
pkgs/development/python-modules/ovoenergy/default.nix-      --replace-fail "==" ">="
pkgs/development/python-modules/ovoenergy/default.nix-  '';
pkgs/development/python-modules/ovoenergy/default.nix-
pkgs/development/python-modules/ovoenergy/default.nix-  build-system = [
pkgs/development/python-modules/ovoenergy/default.nix-    incremental
pkgs/development/python-modules/ovoenergy/default.nix-    setuptools
pkgs/development/python-modules/ovoenergy/default.nix-  ];
pkgs/development/python-modules/ovoenergy/default.nix-
pkgs/development/python-modules/ovoenergy/default.nix-  nativeBuildInputs = [ incremental ];
pkgs/development/python-modules/ovoenergy/default.nix-
--
--
pkgs/development/python-modules/pyfunctional/default.nix-    repo = "PyFunctional";
pkgs/development/python-modules/pyfunctional/default.nix-    rev = "6ed2e9a8a73d97141a8a7edab25e1aefadc256a3"; # missing tag
pkgs/development/python-modules/pyfunctional/default.nix-    hash = "sha256-u7gcZEeg1exb98aVUOorVhxUHqjX50aPTpE5gR6sONI=";
pkgs/development/python-modules/pyfunctional/default.nix-  };
pkgs/development/python-modules/pyfunctional/default.nix-
pkgs/development/python-modules/pyfunctional/default.nix-  build-system = [ poetry-core ];
pkgs/development/python-modules/pyfunctional/default.nix-
pkgs/development/python-modules/pyfunctional/default.nix-  postPatch = ''
pkgs/development/python-modules/pyfunctional/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/pyfunctional/default.nix-      --replace-fail poetry.masonry.api poetry.core.masonry.api \
pkgs/development/python-modules/pyfunctional/default.nix-      --replace-fail "poetry>=" "poetry-core>="
pkgs/development/python-modules/pyfunctional/default.nix-  '';
pkgs/development/python-modules/pyfunctional/default.nix-
pkgs/development/python-modules/pyfunctional/default.nix-  dependencies = [
pkgs/development/python-modules/pyfunctional/default.nix-    dill
pkgs/development/python-modules/pyfunctional/default.nix-    tabulate
pkgs/development/python-modules/pyfunctional/default.nix-  ];
pkgs/development/python-modules/pyfunctional/default.nix-
pkgs/development/python-modules/pyfunctional/default.nix-  nativeCheckInputs = [ pytestCheckHook ];
--
pkgs/development/python-modules/pyfuse3/default.nix-  disabled = pythonOlder "3.8";
--
pkgs/development/python-modules/zigpy-zigate/default.nix-
pkgs/development/python-modules/zigpy-zigate/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/zigpy-zigate/default.nix-    owner = "zigpy";
pkgs/development/python-modules/zigpy-zigate/default.nix-    repo = "zigpy-zigate";
pkgs/development/python-modules/zigpy-zigate/default.nix-    tag = version;
pkgs/development/python-modules/zigpy-zigate/default.nix-    hash = "sha256-reOt0bPPkKDKeu8CESJtLDEmpkOmgopXk65BqBlBIhY=";
pkgs/development/python-modules/zigpy-zigate/default.nix-  };
pkgs/development/python-modules/zigpy-zigate/default.nix-
pkgs/development/python-modules/zigpy-zigate/default.nix-  postPatch = ''
pkgs/development/python-modules/zigpy-zigate/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/zigpy-zigate/default.nix-      --replace ', "setuptools-git-versioning<2"' "" \
pkgs/development/python-modules/zigpy-zigate/default.nix-      --replace 'dynamic = ["version"]' 'version = "${version}"'
pkgs/development/python-modules/zigpy-zigate/default.nix-  '';
pkgs/development/python-modules/zigpy-zigate/default.nix-
pkgs/development/python-modules/zigpy-zigate/default.nix-  nativeBuildInputs = [ setuptools ];
pkgs/development/python-modules/zigpy-zigate/default.nix-
pkgs/development/python-modules/zigpy-zigate/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/zigpy-zigate/default.nix-    gpiozero
pkgs/development/python-modules/zigpy-zigate/default.nix-    pyserial
pkgs/development/python-modules/zigpy-zigate/default.nix-    pyserial-asyncio
--
--
pkgs/development/python-modules/uharfbuzz/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/uharfbuzz/default.nix-    owner = "harfbuzz";
pkgs/development/python-modules/uharfbuzz/default.nix-    repo = "uharfbuzz";
pkgs/development/python-modules/uharfbuzz/default.nix-    tag = "v${version}";
pkgs/development/python-modules/uharfbuzz/default.nix-    fetchSubmodules = true;
pkgs/development/python-modules/uharfbuzz/default.nix-    hash = "sha256-mVxG0unTjMjb0/6w58Py+TARw8YmOWljTlQQwUEdMpg=";
pkgs/development/python-modules/uharfbuzz/default.nix-  };
pkgs/development/python-modules/uharfbuzz/default.nix-
pkgs/development/python-modules/uharfbuzz/default.nix-  postPatch = ''
pkgs/development/python-modules/uharfbuzz/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/uharfbuzz/default.nix-      --replace-fail "setuptools >= 36.4, < 72.2" setuptools
pkgs/development/python-modules/uharfbuzz/default.nix-  '';
pkgs/development/python-modules/uharfbuzz/default.nix-
pkgs/development/python-modules/uharfbuzz/default.nix-  build-system = [
pkgs/development/python-modules/uharfbuzz/default.nix-    cython
pkgs/development/python-modules/uharfbuzz/default.nix-    pkgconfig
pkgs/development/python-modules/uharfbuzz/default.nix-    setuptools
pkgs/development/python-modules/uharfbuzz/default.nix-    setuptools-scm
pkgs/development/python-modules/uharfbuzz/default.nix-  ];
pkgs/development/python-modules/uharfbuzz/default.nix-
--
--
pkgs/development/python-modules/levenshtein/default.nix-
pkgs/development/python-modules/levenshtein/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/levenshtein/default.nix-    owner = "maxbachmann";
pkgs/development/python-modules/levenshtein/default.nix-    repo = "Levenshtein";
pkgs/development/python-modules/levenshtein/default.nix-    tag = "v${version}";
pkgs/development/python-modules/levenshtein/default.nix-    hash = "sha256-EFEyP7eqB4sUQ2ksD67kCr0BEShTiKWbk1PxXOUOGc4=";
pkgs/development/python-modules/levenshtein/default.nix-  };
pkgs/development/python-modules/levenshtein/default.nix-
pkgs/development/python-modules/levenshtein/default.nix-  postPatch = ''
pkgs/development/python-modules/levenshtein/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/levenshtein/default.nix-      --replace-fail "Cython>=3.0.12,<3.1.0" Cython
pkgs/development/python-modules/levenshtein/default.nix-  '';
pkgs/development/python-modules/levenshtein/default.nix-
pkgs/development/python-modules/levenshtein/default.nix-  build-system = [
pkgs/development/python-modules/levenshtein/default.nix-    cmake
pkgs/development/python-modules/levenshtein/default.nix-    cython
pkgs/development/python-modules/levenshtein/default.nix-    ninja
pkgs/development/python-modules/levenshtein/default.nix-    scikit-build-core
pkgs/development/python-modules/levenshtein/default.nix-  ];
pkgs/development/python-modules/levenshtein/default.nix-
--
--
pkgs/development/python-modules/srpenergy/default.nix-
pkgs/development/python-modules/srpenergy/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/srpenergy/default.nix-    owner = "lamoreauxlab";
pkgs/development/python-modules/srpenergy/default.nix-    repo = "srpenergy-api-client-python";
pkgs/development/python-modules/srpenergy/default.nix-    tag = version;
pkgs/development/python-modules/srpenergy/default.nix-    hash = "sha256-bdBF5y9hRj4rceUD5qjHOM9TIaHGElJ36YjWCJgCzX8=";
pkgs/development/python-modules/srpenergy/default.nix-  };
pkgs/development/python-modules/srpenergy/default.nix-
pkgs/development/python-modules/srpenergy/default.nix-  postPatch = ''
pkgs/development/python-modules/srpenergy/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/srpenergy/default.nix-      --replace-fail "setuptools==" "setuptools>="
pkgs/development/python-modules/srpenergy/default.nix-  '';
pkgs/development/python-modules/srpenergy/default.nix-
pkgs/development/python-modules/srpenergy/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/srpenergy/default.nix-
pkgs/development/python-modules/srpenergy/default.nix-  dependencies = [
pkgs/development/python-modules/srpenergy/default.nix-    python-dateutil
pkgs/development/python-modules/srpenergy/default.nix-    requests
pkgs/development/python-modules/srpenergy/default.nix-  ];
pkgs/development/python-modules/srpenergy/default.nix-
--
--
pkgs/development/python-modules/setuptools-scm/default.nix-  src = fetchPypi {
pkgs/development/python-modules/setuptools-scm/default.nix-    pname = "setuptools_scm";
pkgs/development/python-modules/setuptools-scm/default.nix-    inherit version;
pkgs/development/python-modules/setuptools-scm/default.nix-    hash = "sha256-RuHPfooJZSthP5uk/ptV8vSW56Iz5OANJafLQflMPAs=";
pkgs/development/python-modules/setuptools-scm/default.nix-  };
pkgs/development/python-modules/setuptools-scm/default.nix-
pkgs/development/python-modules/setuptools-scm/default.nix-  postPatch =
pkgs/development/python-modules/setuptools-scm/default.nix-    if (pythonOlder "3.11") then
pkgs/development/python-modules/setuptools-scm/default.nix-      ''
pkgs/development/python-modules/setuptools-scm/default.nix:        substituteInPlace pyproject.toml \
pkgs/development/python-modules/setuptools-scm/default.nix-          --replace-fail 'tomli<=2.0.2' 'tomli'
pkgs/development/python-modules/setuptools-scm/default.nix-      ''
pkgs/development/python-modules/setuptools-scm/default.nix-    else
pkgs/development/python-modules/setuptools-scm/default.nix-      null;
pkgs/development/python-modules/setuptools-scm/default.nix-
pkgs/development/python-modules/setuptools-scm/default.nix-  build-system = [ setuptools ] ++ lib.optionals (pythonOlder "3.11") [ tomli ];
pkgs/development/python-modules/setuptools-scm/default.nix-
pkgs/development/python-modules/setuptools-scm/default.nix-  dependencies = [
pkgs/development/python-modules/setuptools-scm/default.nix-    packaging
pkgs/development/python-modules/setuptools-scm/default.nix-    setuptools
--
--
pkgs/development/python-modules/llm/default.nix-      owner = "simonw";
pkgs/development/python-modules/llm/default.nix-      repo = "llm";
pkgs/development/python-modules/llm/default.nix-      tag = version;
pkgs/development/python-modules/llm/default.nix-      hash = "sha256-HWzuPhI+oiCKBeiHK7x9Sc54ZB88Py60FzprMLlZGrY=";
pkgs/development/python-modules/llm/default.nix-    };
pkgs/development/python-modules/llm/default.nix-
pkgs/development/python-modules/llm/default.nix-    patches = [ ./001-disable-install-uninstall-commands.patch ];
pkgs/development/python-modules/llm/default.nix-
pkgs/development/python-modules/llm/default.nix-    postPatch = ''
pkgs/development/python-modules/llm/default.nix:      substituteInPlace llm/cli.py \
pkgs/development/python-modules/llm/default.nix-        --replace-fail "@listOfPackagedPlugins@" "$(< ${listOfPackagedPlugins})"
pkgs/development/python-modules/llm/default.nix-    '';
pkgs/development/python-modules/llm/default.nix-
pkgs/development/python-modules/llm/default.nix-    dependencies = [
pkgs/development/python-modules/llm/default.nix-      click-default-group
pkgs/development/python-modules/llm/default.nix-      condense-json
pkgs/development/python-modules/llm/default.nix-      numpy
pkgs/development/python-modules/llm/default.nix-      openai
pkgs/development/python-modules/llm/default.nix-      pip
pkgs/development/python-modules/llm/default.nix-      pluggy
--
--
pkgs/development/python-modules/pytest-reraise/default.nix-
pkgs/development/python-modules/pytest-reraise/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/pytest-reraise/default.nix-    owner = "bjoluc";
pkgs/development/python-modules/pytest-reraise/default.nix-    repo = pname;
pkgs/development/python-modules/pytest-reraise/default.nix-    tag = "v${version}";
pkgs/development/python-modules/pytest-reraise/default.nix-    hash = "sha256-mgNKoZ+2sinArTZhSwhLxzBTb4QfiT1LWBs7w5MHXWA=";
pkgs/development/python-modules/pytest-reraise/default.nix-  };
pkgs/development/python-modules/pytest-reraise/default.nix-
pkgs/development/python-modules/pytest-reraise/default.nix-  postPatch = ''
pkgs/development/python-modules/pytest-reraise/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/pytest-reraise/default.nix-      --replace-fail 'poetry>=0.12' 'poetry-core>=1.0.0' \
pkgs/development/python-modules/pytest-reraise/default.nix-      --replace-fail 'poetry.masonry' 'poetry.core.masonry'
pkgs/development/python-modules/pytest-reraise/default.nix-  '';
pkgs/development/python-modules/pytest-reraise/default.nix-
pkgs/development/python-modules/pytest-reraise/default.nix-  build-system = [ poetry-core ];
pkgs/development/python-modules/pytest-reraise/default.nix-
pkgs/development/python-modules/pytest-reraise/default.nix-  dependencies = [ pytest ];
pkgs/development/python-modules/pytest-reraise/default.nix-
pkgs/development/python-modules/pytest-reraise/default.nix-  nativeCheckInputs = [ pytestCheckHook ];
pkgs/development/python-modules/pytest-reraise/default.nix-
--
pkgs/development/python-modules/kaptan/default.nix-  format = "pyproject";
pkgs/development/python-modules/kaptan/default.nix-
pkgs/development/python-modules/kaptan/default.nix-  src = fetchPypi {
pkgs/development/python-modules/kaptan/default.nix-    inherit pname version;
pkgs/development/python-modules/kaptan/default.nix-    hash = "sha256-EBMwpE/e3oiFhvMBC9FFwOxIpIBrxWQp+lSHpndAIfg=";
pkgs/development/python-modules/kaptan/default.nix-  };
pkgs/development/python-modules/kaptan/default.nix-
pkgs/development/python-modules/kaptan/default.nix-  postPatch = ''
pkgs/development/python-modules/kaptan/default.nix-    sed -i "s/==.*//g" requirements/test.txt
pkgs/development/python-modules/kaptan/default.nix-
pkgs/development/python-modules/kaptan/default.nix:    substituteInPlace requirements/base.txt --replace 'PyYAML>=3.13,<6' 'PyYAML>=3.13'
pkgs/development/python-modules/kaptan/default.nix-  '';
pkgs/development/python-modules/kaptan/default.nix-
pkgs/development/python-modules/kaptan/default.nix-  nativeBuildInputs = [ setuptools ];
pkgs/development/python-modules/kaptan/default.nix-
pkgs/development/python-modules/kaptan/default.nix-  propagatedBuildInputs = [ pyyaml ];
pkgs/development/python-modules/kaptan/default.nix-
pkgs/development/python-modules/kaptan/default.nix-  nativeCheckInputs = [ pytestCheckHook ];
pkgs/development/python-modules/kaptan/default.nix-
pkgs/development/python-modules/kaptan/default.nix-  meta = with lib; {
pkgs/development/python-modules/kaptan/default.nix-    description = "Configuration manager for python applications";
--
pkgs/development/python-modules/qiskit-optimization/default.nix-  disabled = pythonOlder "3.6";
pkgs/development/python-modules/qiskit-optimization/default.nix-
pkgs/development/python-modules/qiskit-optimization/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/qiskit-optimization/default.nix-    owner = "qiskit";
pkgs/development/python-modules/qiskit-optimization/default.nix-    repo = pname;
pkgs/development/python-modules/qiskit-optimization/default.nix-    rev = "refs/tags/${version}";
pkgs/development/python-modules/qiskit-optimization/default.nix-    hash = "sha256-kzEuICajlV8mgD0YLhwFJaDQVxYZo9jv3sr/r/P0VG0=";
pkgs/development/python-modules/qiskit-optimization/default.nix-  };
pkgs/development/python-modules/qiskit-optimization/default.nix-
pkgs/development/python-modules/qiskit-optimization/default.nix-  postPatch = ''
pkgs/development/python-modules/qiskit-optimization/default.nix:    substituteInPlace requirements.txt --replace "networkx>=2.2,<2.6" "networkx"
pkgs/development/python-modules/qiskit-optimization/default.nix-  '';
pkgs/development/python-modules/qiskit-optimization/default.nix-
pkgs/development/python-modules/qiskit-optimization/default.nix-  nativeBuildInputs = [ setuptools ];
pkgs/development/python-modules/qiskit-optimization/default.nix-
pkgs/development/python-modules/qiskit-optimization/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/qiskit-optimization/default.nix-    docplex
pkgs/development/python-modules/qiskit-optimization/default.nix-    decorator
pkgs/development/python-modules/qiskit-optimization/default.nix-    networkx
pkgs/development/python-modules/qiskit-optimization/default.nix-    numpy
pkgs/development/python-modules/qiskit-optimization/default.nix-    qiskit-terra
--
pkgs/development/python-modules/bellows/default.nix-
pkgs/development/python-modules/bellows/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/bellows/default.nix-    owner = "zigpy";
pkgs/development/python-modules/bellows/default.nix-    repo = "bellows";
pkgs/development/python-modules/bellows/default.nix-    tag = version;
pkgs/development/python-modules/bellows/default.nix-    hash = "sha256-7CU3o7SrBDxgf4Bd7SBkZlfwwdeo1Rr+UyapX3ORyfU=";
pkgs/development/python-modules/bellows/default.nix-  };
pkgs/development/python-modules/bellows/default.nix-
pkgs/development/python-modules/bellows/default.nix-  postPatch = ''
pkgs/development/python-modules/bellows/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/bellows/default.nix-      --replace-fail '"setuptools-git-versioning<2"' "" \
pkgs/development/python-modules/bellows/default.nix-      --replace-fail 'dynamic = ["version"]' 'version = "${version}"'
pkgs/development/python-modules/bellows/default.nix-  '';
pkgs/development/python-modules/bellows/default.nix-
pkgs/development/python-modules/bellows/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/bellows/default.nix-
pkgs/development/python-modules/bellows/default.nix-  dependencies = [
pkgs/development/python-modules/bellows/default.nix-    click
pkgs/development/python-modules/bellows/default.nix-    click-log
pkgs/development/python-modules/bellows/default.nix-    voluptuous
--
--
pkgs/development/python-modules/gipc/default.nix-
pkgs/development/python-modules/gipc/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/gipc/default.nix-    owner = "jgehrcke";
pkgs/development/python-modules/gipc/default.nix-    repo = "gipc";
pkgs/development/python-modules/gipc/default.nix-    tag = version;
pkgs/development/python-modules/gipc/default.nix-    hash = "sha256-eYE7A1VDJ0NSshvdJKxPwGyVdW6BnyWoRSR1i1iTr8Y=";
pkgs/development/python-modules/gipc/default.nix-  };
pkgs/development/python-modules/gipc/default.nix-
pkgs/development/python-modules/gipc/default.nix-  postPatch = ''
pkgs/development/python-modules/gipc/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/gipc/default.nix-      --replace-fail "gevent>=1.5,<=23.9.1" "gevent>=1.5"
pkgs/development/python-modules/gipc/default.nix-  '';
pkgs/development/python-modules/gipc/default.nix-
pkgs/development/python-modules/gipc/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/gipc/default.nix-
pkgs/development/python-modules/gipc/default.nix-  dependencies = [ gevent ];
pkgs/development/python-modules/gipc/default.nix-
pkgs/development/python-modules/gipc/default.nix-  nativeCheckInputs = [ pytestCheckHook ];
pkgs/development/python-modules/gipc/default.nix-
pkgs/development/python-modules/gipc/default.nix-  pythonImportsCheck = [ "gipc" ];
--
--
pkgs/development/python-modules/rapidgzip/default.nix-  disabled = pythonOlder "3.6";
pkgs/development/python-modules/rapidgzip/default.nix-
pkgs/development/python-modules/rapidgzip/default.nix-  src = fetchPypi {
pkgs/development/python-modules/rapidgzip/default.nix-    inherit pname version;
pkgs/development/python-modules/rapidgzip/default.nix-    hash = "sha256-+u1GAToaYqUZPElhWolmg+pcFO1HRLy0vRhpsUIFUdg=";
pkgs/development/python-modules/rapidgzip/default.nix-  };
pkgs/development/python-modules/rapidgzip/default.nix-
pkgs/development/python-modules/rapidgzip/default.nix-  prePatch = ''
pkgs/development/python-modules/rapidgzip/default.nix-    # pythonRelaxDeps doesn't work here
pkgs/development/python-modules/rapidgzip/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/rapidgzip/default.nix-      --replace-fail "setuptools >= 61.2, < 72" "setuptools" \
pkgs/development/python-modules/rapidgzip/default.nix-      --replace-fail "cython >= 3, < 3.1" cython
pkgs/development/python-modules/rapidgzip/default.nix-  '';
pkgs/development/python-modules/rapidgzip/default.nix-
pkgs/development/python-modules/rapidgzip/default.nix-  nativeBuildInputs = [
pkgs/development/python-modules/rapidgzip/default.nix-    cython
pkgs/development/python-modules/rapidgzip/default.nix-    nasm
pkgs/development/python-modules/rapidgzip/default.nix-    setuptools
pkgs/development/python-modules/rapidgzip/default.nix-  ];
pkgs/development/python-modules/rapidgzip/default.nix-
--
pkgs/development/python-modules/radios/default.nix-  disabled = pythonOlder "3.11";
--
pkgs/development/python-modules/protoletariat/default.nix-  ];
--
pkgs/development/python-modules/django-scim2/default.nix-
pkgs/development/python-modules/django-scim2/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/django-scim2/default.nix-    owner = "15five";
pkgs/development/python-modules/django-scim2/default.nix-    repo = "django-scim2";
pkgs/development/python-modules/django-scim2/default.nix-    tag = version;
pkgs/development/python-modules/django-scim2/default.nix-    hash = "sha256-OsfC6Jc/oQl6nzy3Nr3vkY+XicRxUoV62hK8MHa3LJ8=";
pkgs/development/python-modules/django-scim2/default.nix-  };
pkgs/development/python-modules/django-scim2/default.nix-
pkgs/development/python-modules/django-scim2/default.nix-  # remove this when upstream releases a new version > 0.19.0
pkgs/development/python-modules/django-scim2/default.nix-  postPatch = ''
pkgs/development/python-modules/django-scim2/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/django-scim2/default.nix-      --replace-fail "poetry>=0.12" "poetry-core>=1.5.2" \
pkgs/development/python-modules/django-scim2/default.nix-      --replace-fail "poetry.masonry.api" "poetry.core.masonry.api"
pkgs/development/python-modules/django-scim2/default.nix-  '';
pkgs/development/python-modules/django-scim2/default.nix-
pkgs/development/python-modules/django-scim2/default.nix-  build-system = [ poetry-core ];
pkgs/development/python-modules/django-scim2/default.nix-
pkgs/development/python-modules/django-scim2/default.nix-  dependencies = [
pkgs/development/python-modules/django-scim2/default.nix-    django
pkgs/development/python-modules/django-scim2/default.nix-    scim2-filter-parser
pkgs/development/python-modules/django-scim2/default.nix-  ];
--
--
pkgs/development/python-modules/nidaqmx/default.nix-
pkgs/development/python-modules/nidaqmx/default.nix-  disabled = pythonOlder "3.8";
pkgs/development/python-modules/nidaqmx/default.nix-
pkgs/development/python-modules/nidaqmx/default.nix-  build-system = [ poetry-core ];
pkgs/development/python-modules/nidaqmx/default.nix-
pkgs/development/python-modules/nidaqmx/default.nix-  prePatch = ''
pkgs/development/python-modules/nidaqmx/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/nidaqmx/default.nix-      --replace-fail 'poetry.masonry.api' 'poetry.core.masonry.api'
pkgs/development/python-modules/nidaqmx/default.nix-
pkgs/development/python-modules/nidaqmx/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/nidaqmx/default.nix-      --replace-fail '["poetry>=1.2"]' '["poetry-core>=1.0.0"]'
pkgs/development/python-modules/nidaqmx/default.nix-  '';
pkgs/development/python-modules/nidaqmx/default.nix-
pkgs/development/python-modules/nidaqmx/default.nix-  dependencies = [
pkgs/development/python-modules/nidaqmx/default.nix-    numpy
pkgs/development/python-modules/nidaqmx/default.nix-    deprecation
pkgs/development/python-modules/nidaqmx/default.nix-    hightime
pkgs/development/python-modules/nidaqmx/default.nix-    tzlocal
pkgs/development/python-modules/nidaqmx/default.nix-    python-decouple
pkgs/development/python-modules/nidaqmx/default.nix-    click
--
--
pkgs/development/python-modules/py-cid/default.nix-
pkgs/development/python-modules/py-cid/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/py-cid/default.nix-    owner = "ipld";
pkgs/development/python-modules/py-cid/default.nix-    repo = "py-cid";
pkgs/development/python-modules/py-cid/default.nix-    rev = "v${version}";
pkgs/development/python-modules/py-cid/default.nix-    hash = "sha256-aN7ee25ghKKa90+FoMDCdGauToePc5AzDLV3tONvh4U=";
pkgs/development/python-modules/py-cid/default.nix-  };
pkgs/development/python-modules/py-cid/default.nix-
pkgs/development/python-modules/py-cid/default.nix-  postPatch = ''
pkgs/development/python-modules/py-cid/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/py-cid/default.nix-      --replace "base58>=1.0.2,<2.0" "base58>=1.0.2" \
pkgs/development/python-modules/py-cid/default.nix-      --replace "py-multihash>=0.2.0,<1.0.0" "py-multihash>=0.2.0" \
pkgs/development/python-modules/py-cid/default.nix-      --replace "'pytest-runner'," ""
pkgs/development/python-modules/py-cid/default.nix-  '';
pkgs/development/python-modules/py-cid/default.nix-
pkgs/development/python-modules/py-cid/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/py-cid/default.nix-    base58
pkgs/development/python-modules/py-cid/default.nix-    py-multibase
pkgs/development/python-modules/py-cid/default.nix-    py-multicodec
pkgs/development/python-modules/py-cid/default.nix-    morphys
--
pkgs/development/python-modules/pycategories/default.nix-  format = "setuptools";
--
pkgs/development/python-modules/pyspark/default.nix-  src = fetchPypi {
pkgs/development/python-modules/pyspark/default.nix-    inherit pname version;
pkgs/development/python-modules/pyspark/default.nix-    hash = "sha256-bv/Jzpjt8jH01oP9FPcnBim/hFjGKNaiYg3tS7NPPLk=";
pkgs/development/python-modules/pyspark/default.nix-  };
pkgs/development/python-modules/pyspark/default.nix-
pkgs/development/python-modules/pyspark/default.nix-  # pypandoc is broken with pandoc2, so we just lose docs.
pkgs/development/python-modules/pyspark/default.nix-  postPatch = ''
pkgs/development/python-modules/pyspark/default.nix-    sed -i "s/'pypandoc'//" setup.py
pkgs/development/python-modules/pyspark/default.nix-
pkgs/development/python-modules/pyspark/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/pyspark/default.nix-      --replace py4j== 'py4j>='
pkgs/development/python-modules/pyspark/default.nix-  '';
pkgs/development/python-modules/pyspark/default.nix-
pkgs/development/python-modules/pyspark/default.nix-  postFixup = ''
pkgs/development/python-modules/pyspark/default.nix-    # find_python_home.py has been wrapped as a shell script
pkgs/development/python-modules/pyspark/default.nix:    substituteInPlace $out/bin/find-spark-home \
pkgs/development/python-modules/pyspark/default.nix-        --replace 'export SPARK_HOME=$($PYSPARK_DRIVER_PYTHON "$FIND_SPARK_HOME_PYTHON_SCRIPT")' \
pkgs/development/python-modules/pyspark/default.nix-                  'export SPARK_HOME=$("$FIND_SPARK_HOME_PYTHON_SCRIPT")'
pkgs/development/python-modules/pyspark/default.nix-    # patch PYTHONPATH in pyspark so that it properly looks at SPARK_HOME
pkgs/development/python-modules/pyspark/default.nix:    substituteInPlace $out/bin/pyspark \
pkgs/development/python-modules/pyspark/default.nix-        --replace 'export PYTHONPATH="''${SPARK_HOME}/python/:$PYTHONPATH"' \
--
pkgs/development/python-modules/cynthion/default.nix-    owner = "greatscottgadgets";
pkgs/development/python-modules/cynthion/default.nix-    repo = "cynthion";
pkgs/development/python-modules/cynthion/default.nix-    tag = version;
pkgs/development/python-modules/cynthion/default.nix-    hash = "sha256-NAsELeOnWgMa6iWCJ0+hpbHIO3BsZBv0N/nK1XP+IpU=";
pkgs/development/python-modules/cynthion/default.nix-  };
pkgs/development/python-modules/cynthion/default.nix-
pkgs/development/python-modules/cynthion/default.nix-  sourceRoot = "${src.name}/cynthion/python";
pkgs/development/python-modules/cynthion/default.nix-
pkgs/development/python-modules/cynthion/default.nix-  postPatch = ''
pkgs/development/python-modules/cynthion/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/cynthion/default.nix-      --replace-fail '"setuptools-git-versioning<2"' "" \
pkgs/development/python-modules/cynthion/default.nix-      --replace-fail 'dynamic = ["version"]' 'version = "${version}"'
pkgs/development/python-modules/cynthion/default.nix-  '';
pkgs/development/python-modules/cynthion/default.nix-
pkgs/development/python-modules/cynthion/default.nix-  nativeBuildInputs = [ udevCheckHook ];
pkgs/development/python-modules/cynthion/default.nix-
pkgs/development/python-modules/cynthion/default.nix-  build-system = [
pkgs/development/python-modules/cynthion/default.nix-    setuptools
pkgs/development/python-modules/cynthion/default.nix-  ];
pkgs/development/python-modules/cynthion/default.nix-
--
--
pkgs/development/python-modules/translatehtml/default.nix-
pkgs/development/python-modules/translatehtml/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/translatehtml/default.nix-    argostranslate
pkgs/development/python-modules/translatehtml/default.nix-    beautifulsoup4
pkgs/development/python-modules/translatehtml/default.nix-  ];
pkgs/development/python-modules/translatehtml/default.nix-
pkgs/development/python-modules/translatehtml/default.nix-  postPatch = ''
pkgs/development/python-modules/translatehtml/default.nix-    ln -s */requires.txt requirements.txt
pkgs/development/python-modules/translatehtml/default.nix-
pkgs/development/python-modules/translatehtml/default.nix:    substituteInPlace requirements.txt  \
pkgs/development/python-modules/translatehtml/default.nix-      --replace "==" ">="
pkgs/development/python-modules/translatehtml/default.nix-  '';
pkgs/development/python-modules/translatehtml/default.nix-
pkgs/development/python-modules/translatehtml/default.nix-  # required for import check to work (argostranslate)
pkgs/development/python-modules/translatehtml/default.nix-  env.HOME = "/tmp";
pkgs/development/python-modules/translatehtml/default.nix-
pkgs/development/python-modules/translatehtml/default.nix-  pythonImportsCheck = [ "translatehtml" ];
pkgs/development/python-modules/translatehtml/default.nix-
pkgs/development/python-modules/translatehtml/default.nix-  doCheck = false; # no tests
pkgs/development/python-modules/translatehtml/default.nix-
--
pkgs/development/python-modules/ansible/core.nix-
pkgs/development/python-modules/ansible/core.nix-    SETUPTOOLS_PATTERN='"setuptools[0-9 <>=.,]+"'
pkgs/development/python-modules/ansible/core.nix-    PYPROJECT=$(cat pyproject.toml)
pkgs/development/python-modules/ansible/core.nix-    if [[ "$PYPROJECT" =~ $SETUPTOOLS_PATTERN ]]; then
pkgs/development/python-modules/ansible/core.nix-      echo "setuptools replace: ''${BASH_REMATCH[0]}"
pkgs/development/python-modules/ansible/core.nix-      echo "''${PYPROJECT//''${BASH_REMATCH[0]}/'"setuptools"'}" > pyproject.toml
pkgs/development/python-modules/ansible/core.nix-    else
pkgs/development/python-modules/ansible/core.nix-      exit 2
pkgs/development/python-modules/ansible/core.nix-    fi
pkgs/development/python-modules/ansible/core.nix-
pkgs/development/python-modules/ansible/core.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/ansible/core.nix-      --replace-fail "wheel == 0.45.1" wheel
pkgs/development/python-modules/ansible/core.nix-  '';
pkgs/development/python-modules/ansible/core.nix-
pkgs/development/python-modules/ansible/core.nix-  nativeBuildInputs = [
pkgs/development/python-modules/ansible/core.nix-    installShellFiles
--
pkgs/development/python-modules/ruff/default.nix-    ''
pkgs/development/python-modules/ruff/default.nix:      substituteInPlace python/ruff/__main__.py \
pkgs/development/python-modules/ruff/default.nix-        --replace-fail \
pkgs/development/python-modules/ruff/default.nix-          'ruff_exe = "ruff" + sysconfig.get_config_var("EXE")' \
pkgs/development/python-modules/ruff/default.nix-          'return "${lib.getExe ruff}"'
pkgs/development/python-modules/ruff/default.nix-    ''
pkgs/development/python-modules/ruff/default.nix-    # Sidestep the maturin build system in favour of reusing the binary already built by nixpkgs,
pkgs/development/python-modules/ruff/default.nix-    # to avoid rebuilding the ruff binary for every active python package set.
pkgs/development/python-modules/ruff/default.nix-    + ''
pkgs/development/python-modules/ruff/default.nix:      substituteInPlace pyproject.toml \
pkgs/development/python-modules/ruff/default.nix-        --replace-fail 'requires = ["maturin>=1.9,<2.0"]' 'requires = ["hatchling"]' \
pkgs/development/python-modules/ruff/default.nix-        --replace-fail 'build-backend = "maturin"' 'build-backend = "hatchling.build"'
pkgs/development/python-modules/ruff/default.nix-
pkgs/development/python-modules/ruff/default.nix-      cat >> pyproject.toml <<EOF
pkgs/development/python-modules/ruff/default.nix-      [tool.hatch.build]
pkgs/development/python-modules/ruff/default.nix-      packages = ['python/ruff']
pkgs/development/python-modules/ruff/default.nix-
pkgs/development/python-modules/ruff/default.nix-      EOF
pkgs/development/python-modules/ruff/default.nix-    '';
pkgs/development/python-modules/ruff/default.nix-
--
pkgs/development/python-modules/dash/default.nix-  yarnOfflineCache = fetchYarnDeps {
pkgs/development/python-modules/dash/default.nix-    yarnLock = "${src}/@plotly/dash-jupyterlab/yarn.lock";
pkgs/development/python-modules/dash/default.nix-    hash = "sha256-Nvm9BS55q/HW9ArpHD01F5Rmx8PLS3yqaz1yDK8Sg68=";
--
pkgs/development/python-modules/sqlmap/default.nix-    inherit pname version;
pkgs/development/python-modules/sqlmap/default.nix-    hash = "sha256-CQiJ/8MtsoGcfnVA3hI4KZaX+p0ihQmasfwgOTd9we8=";
pkgs/development/python-modules/sqlmap/default.nix-  };
pkgs/development/python-modules/sqlmap/default.nix-
pkgs/development/python-modules/sqlmap/default.nix-  postPatch = ''
pkgs/development/python-modules/sqlmap/default.nix:    substituteInPlace sqlmap/thirdparty/magic/magic.py --replace "ctypes.util.find_library('magic')" \
pkgs/development/python-modules/sqlmap/default.nix-      "'${file}/lib/libmagic${stdenv.hostPlatform.extensions.sharedLibrary}'"
pkgs/development/python-modules/sqlmap/default.nix-
pkgs/development/python-modules/sqlmap/default.nix-    # the check for the last update date does not work in Nix,
pkgs/development/python-modules/sqlmap/default.nix-    # since the timestamp of the all files in the nix store is reset to the unix epoch
pkgs/development/python-modules/sqlmap/default.nix-    echo 'LAST_UPDATE_NAGGING_DAYS = float("inf")' >> sqlmap/lib/core/settings.py
pkgs/development/python-modules/sqlmap/default.nix-  '';
pkgs/development/python-modules/sqlmap/default.nix-
pkgs/development/python-modules/sqlmap/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/sqlmap/default.nix-
pkgs/development/python-modules/sqlmap/default.nix-  # No tests in archive
--
pkgs/development/python-modules/cyclonedds-python/default.nix-  pyproject = true;
pkgs/development/python-modules/cyclonedds-python/default.nix-
pkgs/development/python-modules/cyclonedds-python/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/cyclonedds-python/default.nix-    owner = "eclipse-cyclonedds";
--
pkgs/development/python-modules/cyclonedds-python/default.nix-  env.CYCLONEDDS_HOME = "${cyclonedds.out}";
--
pkgs/development/python-modules/kinparse/default.nix-
pkgs/development/python-modules/kinparse/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/kinparse/default.nix-    owner = "xesscorp";
pkgs/development/python-modules/kinparse/default.nix-    repo = "kinparse";
pkgs/development/python-modules/kinparse/default.nix-    tag = version;
pkgs/development/python-modules/kinparse/default.nix-    hash = "sha256-170e2uhqpk6u/hahivWYubr3Ptb8ijymJSxhxrAfuyI=";
pkgs/development/python-modules/kinparse/default.nix-  };
pkgs/development/python-modules/kinparse/default.nix-
pkgs/development/python-modules/kinparse/default.nix-  # Remove python2 build support as it breaks python >= 3.13
pkgs/development/python-modules/kinparse/default.nix-  postPatch = ''
pkgs/development/python-modules/kinparse/default.nix:    substituteInPlace setup.cfg \
pkgs/development/python-modules/kinparse/default.nix-      --replace-fail "universal = 1" "universal = 0"
pkgs/development/python-modules/kinparse/default.nix-  '';
pkgs/development/python-modules/kinparse/default.nix-
pkgs/development/python-modules/kinparse/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/kinparse/default.nix-
pkgs/development/python-modules/kinparse/default.nix-  dependencies = [ pyparsing ];
pkgs/development/python-modules/kinparse/default.nix-
pkgs/development/python-modules/kinparse/default.nix-  pythonRemoveDeps = [ "future" ];
--
pkgs/development/python-modules/fastmcp/default.nix-
pkgs/development/python-modules/fastmcp/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/fastmcp/default.nix-    owner = "jlowin";
pkgs/development/python-modules/fastmcp/default.nix-    repo = "fastmcp";
pkgs/development/python-modules/fastmcp/default.nix-    tag = "v${version}";
pkgs/development/python-modules/fastmcp/default.nix-    hash = "sha256-jIXrMyNnyPE2DUgg+sxT6LD4dTmKQglh4cFuaw179Z0=";
pkgs/development/python-modules/fastmcp/default.nix-  };
pkgs/development/python-modules/fastmcp/default.nix-
pkgs/development/python-modules/fastmcp/default.nix-  postPatch = ''
pkgs/development/python-modules/fastmcp/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/fastmcp/default.nix-      --replace-fail ', "uv-dynamic-versioning>=0.7.0"' "" \
pkgs/development/python-modules/fastmcp/default.nix-      --replace-fail 'dynamic = ["version"]' 'version = "${version}"'
pkgs/development/python-modules/fastmcp/default.nix-  '';
pkgs/development/python-modules/fastmcp/default.nix-
pkgs/development/python-modules/fastmcp/default.nix-  build-system = [
pkgs/development/python-modules/fastmcp/default.nix-    hatchling
pkgs/development/python-modules/fastmcp/default.nix-  ];
pkgs/development/python-modules/fastmcp/default.nix-
pkgs/development/python-modules/fastmcp/default.nix-  dependencies = [
pkgs/development/python-modules/fastmcp/default.nix-    authlib
--
--
pkgs/development/python-modules/namedlist/default.nix-
pkgs/development/python-modules/namedlist/default.nix-  meta = with lib; {
--
pkgs/development/python-modules/nanoeigenpy/default.nix-    owner = "Simple-Robotics";
pkgs/development/python-modules/nanoeigenpy/default.nix-    repo = "nanoeigenpy";
pkgs/development/python-modules/nanoeigenpy/default.nix-    tag = "v${version}";
pkgs/development/python-modules/nanoeigenpy/default.nix-    hash = "sha256-2Lp3fYw3rQYxjkCQCeHI+N32Y4vTJ8l+PoKqLCmAXIU=";
pkgs/development/python-modules/nanoeigenpy/default.nix-  };
pkgs/development/python-modules/nanoeigenpy/default.nix-
pkgs/development/python-modules/nanoeigenpy/default.nix-  # Fix:
pkgs/development/python-modules/nanoeigenpy/default.nix-  # > PermissionError: [Errno 13] Permission denied:
pkgs/development/python-modules/nanoeigenpy/default.nix-  # > '/nix/store/…-python3-3.12.9/lib/python3.12/site-packages/nanoeigenpy.pyi'
pkgs/development/python-modules/nanoeigenpy/default.nix-  postPatch = ''
pkgs/development/python-modules/nanoeigenpy/default.nix:    substituteInPlace CMakeLists.txt --replace-fail \
pkgs/development/python-modules/nanoeigenpy/default.nix-      "$""{Python_SITELIB}" \
pkgs/development/python-modules/nanoeigenpy/default.nix-      "${python.sitePackages}"
pkgs/development/python-modules/nanoeigenpy/default.nix-  '';
pkgs/development/python-modules/nanoeigenpy/default.nix-
pkgs/development/python-modules/nanoeigenpy/default.nix-  outputs = [
pkgs/development/python-modules/nanoeigenpy/default.nix-    "dev"
pkgs/development/python-modules/nanoeigenpy/default.nix-    "doc"
pkgs/development/python-modules/nanoeigenpy/default.nix-    "out"
--
pkgs/development/python-modules/graphlib-backport/default.nix-
pkgs/development/python-modules/graphlib-backport/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/graphlib-backport/default.nix-    owner = "mariushelf";
pkgs/development/python-modules/graphlib-backport/default.nix-    repo = "graphlib_backport";
pkgs/development/python-modules/graphlib-backport/default.nix-    rev = version;
pkgs/development/python-modules/graphlib-backport/default.nix-    hash = "sha256-ssJLtBQH8sSnccgcAKLKfYpPyw5U0RIm1F66/Er81lo=";
pkgs/development/python-modules/graphlib-backport/default.nix-  };
pkgs/development/python-modules/graphlib-backport/default.nix-
pkgs/development/python-modules/graphlib-backport/default.nix-  postPatch = ''
pkgs/development/python-modules/graphlib-backport/default.nix:    substituteInPlace pyproject.toml        \
pkgs/development/python-modules/graphlib-backport/default.nix-      --replace 'poetry>=1.0' 'poetry-core' \
pkgs/development/python-modules/graphlib-backport/default.nix-      --replace 'poetry.masonry.api' 'poetry.core.masonry.api'
pkgs/development/python-modules/graphlib-backport/default.nix-  '';
pkgs/development/python-modules/graphlib-backport/default.nix-
pkgs/development/python-modules/graphlib-backport/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/graphlib-backport/default.nix-    setuptools
pkgs/development/python-modules/graphlib-backport/default.nix-    poetry-core
pkgs/development/python-modules/graphlib-backport/default.nix-  ];
pkgs/development/python-modules/graphlib-backport/default.nix-
pkgs/development/python-modules/graphlib-backport/default.nix-  pythonImportsCheck = [ "graphlib" ];
--
--
pkgs/development/python-modules/greatfet/default.nix-    owner = "greatscottgadgets";
pkgs/development/python-modules/greatfet/default.nix-    repo = "greatfet";
pkgs/development/python-modules/greatfet/default.nix-    tag = "v${version}";
pkgs/development/python-modules/greatfet/default.nix-    hash = "sha256-3ClM4UzVIDEkVBrFwzvLokbxUHXqdQWyNVqcFtiXCOQ=";
pkgs/development/python-modules/greatfet/default.nix-  };
pkgs/development/python-modules/greatfet/default.nix-
pkgs/development/python-modules/greatfet/default.nix-  sourceRoot = "${src.name}/host";
pkgs/development/python-modules/greatfet/default.nix-
pkgs/development/python-modules/greatfet/default.nix-  postPatch = ''
pkgs/development/python-modules/greatfet/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/greatfet/default.nix-      --replace-fail ', "setuptools-git-versioning<2"' "" \
pkgs/development/python-modules/greatfet/default.nix-      --replace-fail 'dynamic = ["version"]' 'version = "${version}"'
pkgs/development/python-modules/greatfet/default.nix-  '';
pkgs/development/python-modules/greatfet/default.nix-
pkgs/development/python-modules/greatfet/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/greatfet/default.nix-
pkgs/development/python-modules/greatfet/default.nix-  pythonRelaxDeps = [ "ipython" ];
pkgs/development/python-modules/greatfet/default.nix-
pkgs/development/python-modules/greatfet/default.nix-  dependencies = [
pkgs/development/python-modules/greatfet/default.nix-    cmsis-svd
--
--
pkgs/development/python-modules/pyfwup/default.nix-
pkgs/development/python-modules/pyfwup/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/pyfwup/default.nix-    owner = "greatscottgadgets";
pkgs/development/python-modules/pyfwup/default.nix-    repo = "pyfwup";
pkgs/development/python-modules/pyfwup/default.nix-    tag = version;
pkgs/development/python-modules/pyfwup/default.nix-    hash = "sha256-Kyc3f8beTg0W1+U7SvZuNPN1pdsco9rBUfoEtR7AI44=";
pkgs/development/python-modules/pyfwup/default.nix-  };
pkgs/development/python-modules/pyfwup/default.nix-
pkgs/development/python-modules/pyfwup/default.nix-  postPatch = ''
pkgs/development/python-modules/pyfwup/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/pyfwup/default.nix-      --replace-fail '"setuptools-git-versioning<2"' "" \
pkgs/development/python-modules/pyfwup/default.nix-      --replace-fail 'dynamic = ["version"]' 'version = "${version}"'
pkgs/development/python-modules/pyfwup/default.nix-  '';
pkgs/development/python-modules/pyfwup/default.nix-
pkgs/development/python-modules/pyfwup/default.nix-  dependencies = [
pkgs/development/python-modules/pyfwup/default.nix-    pyusb
pkgs/development/python-modules/pyfwup/default.nix-    tqdm
pkgs/development/python-modules/pyfwup/default.nix-    libusb1
pkgs/development/python-modules/pyfwup/default.nix-  ];
pkgs/development/python-modules/pyfwup/default.nix-
--
--
pkgs/development/python-modules/trezor-agent/default.nix-    mnemonic
pkgs/development/python-modules/trezor-agent/default.nix-    keepkey
pkgs/development/python-modules/trezor-agent/default.nix-    semver
pkgs/development/python-modules/trezor-agent/default.nix-    wheel
pkgs/development/python-modules/trezor-agent/default.nix-    pinentry
pkgs/development/python-modules/trezor-agent/default.nix-  ];
pkgs/development/python-modules/trezor-agent/default.nix-
pkgs/development/python-modules/trezor-agent/default.nix-  # relax dependency constraint
pkgs/development/python-modules/trezor-agent/default.nix-  postPatch = ''
pkgs/development/python-modules/trezor-agent/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/trezor-agent/default.nix-      --replace "trezor[hidapi]>=0.12.0,<0.13" "trezor[hidapi]>=0.12.0,<0.14"
pkgs/development/python-modules/trezor-agent/default.nix-  '';
pkgs/development/python-modules/trezor-agent/default.nix-
pkgs/development/python-modules/trezor-agent/default.nix-  doCheck = false;
pkgs/development/python-modules/trezor-agent/default.nix-  pythonImportsCheck = [ "libagent" ];
pkgs/development/python-modules/trezor-agent/default.nix-
pkgs/development/python-modules/trezor-agent/default.nix-  meta = with lib; {
pkgs/development/python-modules/trezor-agent/default.nix-    description = "Using Trezor as hardware SSH agent";
pkgs/development/python-modules/trezor-agent/default.nix-    homepage = "https://github.com/romanz/trezor-agent";
pkgs/development/python-modules/trezor-agent/default.nix-    license = licenses.gpl3;
--
--
pkgs/development/python-modules/grpcio-testing/default.nix-  disabled = pythonOlder "3.7";
pkgs/development/python-modules/grpcio-testing/default.nix-
pkgs/development/python-modules/grpcio-testing/default.nix-  src = fetchPypi {
pkgs/development/python-modules/grpcio-testing/default.nix-    pname = "grpcio_testing";
pkgs/development/python-modules/grpcio-testing/default.nix-    inherit version;
pkgs/development/python-modules/grpcio-testing/default.nix-    hash = "sha256-Ed7bU6QQ/jsqK8mp7ZyaaXlCDJMkPafXh/fM+aJUPjc=";
pkgs/development/python-modules/grpcio-testing/default.nix-  };
pkgs/development/python-modules/grpcio-testing/default.nix-
pkgs/development/python-modules/grpcio-testing/default.nix-  postPatch = ''
pkgs/development/python-modules/grpcio-testing/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/grpcio-testing/default.nix-      --replace-fail '"grpcio>={version}".format(version=grpc_version.VERSION)' '"grpcio"'
pkgs/development/python-modules/grpcio-testing/default.nix-  '';
pkgs/development/python-modules/grpcio-testing/default.nix-
pkgs/development/python-modules/grpcio-testing/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/grpcio-testing/default.nix-
pkgs/development/python-modules/grpcio-testing/default.nix-  pythonRelaxDeps = [
pkgs/development/python-modules/grpcio-testing/default.nix-    "protobuf"
pkgs/development/python-modules/grpcio-testing/default.nix-  ];
pkgs/development/python-modules/grpcio-testing/default.nix-
pkgs/development/python-modules/grpcio-testing/default.nix-  dependencies = [
--
--
pkgs/development/python-modules/chalice/default.nix-
pkgs/development/python-modules/chalice/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/chalice/default.nix-    owner = "aws";
pkgs/development/python-modules/chalice/default.nix-    repo = "chalice";
pkgs/development/python-modules/chalice/default.nix-    tag = version;
pkgs/development/python-modules/chalice/default.nix-    hash = "sha256-m3pSD4fahBW6Yt/w07Co4fTZD7k6as5cPwoK5QSry6M=";
pkgs/development/python-modules/chalice/default.nix-  };
pkgs/development/python-modules/chalice/default.nix-
pkgs/development/python-modules/chalice/default.nix-  postPatch = ''
pkgs/development/python-modules/chalice/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/chalice/default.nix-      --replace "inquirer>=2.7.0,<3.0.0" "inquirer" \
pkgs/development/python-modules/chalice/default.nix-      --replace "pip>=9,<23.1" "pip" \
pkgs/development/python-modules/chalice/default.nix-  '';
pkgs/development/python-modules/chalice/default.nix-
pkgs/development/python-modules/chalice/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/chalice/default.nix-    attrs
pkgs/development/python-modules/chalice/default.nix-    botocore
pkgs/development/python-modules/chalice/default.nix-    click
pkgs/development/python-modules/chalice/default.nix-    inquirer
pkgs/development/python-modules/chalice/default.nix-    jmespath
--
pkgs/development/python-modules/fs/default.nix-
--
pkgs/development/python-modules/mip/default.nix-  patches = [
pkgs/development/python-modules/mip/default.nix-    # Some tests try to be smart and dynamically construct a path to their test
pkgs/development/python-modules/mip/default.nix-    # inputs. Unfortunately, since the test phase is run after installation,
pkgs/development/python-modules/mip/default.nix-    # those paths point to the Nix store, which no longer contains the test
pkgs/development/python-modules/mip/default.nix-    # data. This patch hardcodes the data path to point to the source directory.
pkgs/development/python-modules/mip/default.nix-    ./test-data-path.patch
pkgs/development/python-modules/mip/default.nix-  ];
pkgs/development/python-modules/mip/default.nix-
pkgs/development/python-modules/mip/default.nix-  postPatch = ''
pkgs/development/python-modules/mip/default.nix-    # Allow newer cffi versions to be used
pkgs/development/python-modules/mip/default.nix:    substituteInPlace pyproject.toml --replace "cffi==1.15.*" "cffi>=1.15"
pkgs/development/python-modules/mip/default.nix-  '';
pkgs/development/python-modules/mip/default.nix-
pkgs/development/python-modules/mip/default.nix-  # Make MIP use the Gurobi solver, if configured to do so
pkgs/development/python-modules/mip/default.nix-  makeWrapperArgs = lib.optional gurobiSupport "--set GUROBI_HOME ${
pkgs/development/python-modules/mip/default.nix-    if gurobiHome == null then gurobi.outPath else gurobiHome
pkgs/development/python-modules/mip/default.nix-  }";
pkgs/development/python-modules/mip/default.nix-
pkgs/development/python-modules/mip/default.nix-  # Tests that rely on Gurobi are activated only when Gurobi support is enabled
pkgs/development/python-modules/mip/default.nix-  disabledTests = lib.optional (!gurobiSupport) "gurobi";
pkgs/development/python-modules/mip/default.nix-
--
pkgs/development/python-modules/heudiconv/default.nix-
pkgs/development/python-modules/heudiconv/default.nix-  disabled = pythonOlder "3.8";
pkgs/development/python-modules/heudiconv/default.nix-
pkgs/development/python-modules/heudiconv/default.nix-  src = fetchPypi {
pkgs/development/python-modules/heudiconv/default.nix-    inherit pname version;
pkgs/development/python-modules/heudiconv/default.nix-    hash = "sha256-SnYysTsQUagXH8CCPgNoca2ls47XUguE/pJD2wc1tro=";
pkgs/development/python-modules/heudiconv/default.nix-  };
pkgs/development/python-modules/heudiconv/default.nix-
pkgs/development/python-modules/heudiconv/default.nix-  postPatch = ''
pkgs/development/python-modules/heudiconv/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/heudiconv/default.nix-      --replace-fail "versioningit ~=" "versioningit >="
pkgs/development/python-modules/heudiconv/default.nix-  '';
pkgs/development/python-modules/heudiconv/default.nix-
pkgs/development/python-modules/heudiconv/default.nix-  build-system = [
pkgs/development/python-modules/heudiconv/default.nix-    setuptools
pkgs/development/python-modules/heudiconv/default.nix-    versioningit
pkgs/development/python-modules/heudiconv/default.nix-  ];
pkgs/development/python-modules/heudiconv/default.nix-
pkgs/development/python-modules/heudiconv/default.nix-  dependencies = [
pkgs/development/python-modules/heudiconv/default.nix-    dcmstack
--
--
pkgs/development/python-modules/zope-testrunner/default.nix-
pkgs/development/python-modules/zope-testrunner/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/zope-testrunner/default.nix-    owner = "zopefoundation";
pkgs/development/python-modules/zope-testrunner/default.nix-    repo = "zope.testrunner";
pkgs/development/python-modules/zope-testrunner/default.nix-    tag = version;
pkgs/development/python-modules/zope-testrunner/default.nix-    hash = "sha256-cvZXQzbIUBq99P0FYSydG1tLNBMFTTvuMvqWGaNFhJc=";
pkgs/development/python-modules/zope-testrunner/default.nix-  };
pkgs/development/python-modules/zope-testrunner/default.nix-
pkgs/development/python-modules/zope-testrunner/default.nix-  postPatch = ''
pkgs/development/python-modules/zope-testrunner/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/zope-testrunner/default.nix-      --replace-fail "setuptools<74" "setuptools"
pkgs/development/python-modules/zope-testrunner/default.nix-  '';
pkgs/development/python-modules/zope-testrunner/default.nix-
pkgs/development/python-modules/zope-testrunner/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/zope-testrunner/default.nix-
pkgs/development/python-modules/zope-testrunner/default.nix-  dependencies = [
pkgs/development/python-modules/zope-testrunner/default.nix-    zope-interface
pkgs/development/python-modules/zope-testrunner/default.nix-    zope-exceptions
pkgs/development/python-modules/zope-testrunner/default.nix-  ];
pkgs/development/python-modules/zope-testrunner/default.nix-
--
--
pkgs/development/python-modules/pyfluidsynth/default.nix-        '"${lib.getLib fluidsynth}/lib/libfluidsynth${stdenv.hostPlatform.extensions.sharedLibrary}"'
pkgs/development/python-modules/pyfluidsynth/default.nix-  '';
pkgs/development/python-modules/pyfluidsynth/default.nix-
pkgs/development/python-modules/pyfluidsynth/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/pyfluidsynth/default.nix-
pkgs/development/python-modules/pyfluidsynth/default.nix-  dependencies = [ numpy ];
pkgs/development/python-modules/pyfluidsynth/default.nix-
pkgs/development/python-modules/pyfluidsynth/default.nix-  pythonImportsCheck = [ "fluidsynth" ];
--
pkgs/development/python-modules/sipsimple/default.nix-  patches = [
pkgs/development/python-modules/sipsimple/default.nix-    # Remove when version > 5.3.3.2-mac
pkgs/development/python-modules/sipsimple/default.nix-    (fetchpatch {
pkgs/development/python-modules/sipsimple/default.nix-      name = "0001-python3-sipsimple-port-to-cython-3.patch";
pkgs/development/python-modules/sipsimple/default.nix-      url = "https://github.com/AGProjects/python3-sipsimple/commit/ccbbbb0225b2417bdf6ae07da96bffe367e242be.patch";
pkgs/development/python-modules/sipsimple/default.nix-      hash = "sha256-MBiM9/yS5yX9QoZT7p76PI2rbBr22fZw6TAT4tw9iZk=";
pkgs/development/python-modules/sipsimple/default.nix-    })
pkgs/development/python-modules/sipsimple/default.nix-  ];
pkgs/development/python-modules/sipsimple/default.nix-
pkgs/development/python-modules/sipsimple/default.nix-  postPatch = ''
pkgs/development/python-modules/sipsimple/default.nix:    substituteInPlace get_dependencies.sh \
pkgs/development/python-modules/sipsimple/default.nix-      --replace-fail 'sudo apt' 'echo Skipping sudo apt'
--
pkgs/development/python-modules/jupyterlab-pygments/default.nix-
pkgs/development/python-modules/jupyterlab-pygments/default.nix-  src = fetchPypi {
pkgs/development/python-modules/jupyterlab-pygments/default.nix-    pname = "jupyterlab_pygments";
pkgs/development/python-modules/jupyterlab-pygments/default.nix-    inherit version;
pkgs/development/python-modules/jupyterlab-pygments/default.nix-    hash = "sha256-chrKTZApJSsRz6nRheW1r01Udyu4By+bcDb0FwBU010=";
pkgs/development/python-modules/jupyterlab-pygments/default.nix-  };
pkgs/development/python-modules/jupyterlab-pygments/default.nix-
pkgs/development/python-modules/jupyterlab-pygments/default.nix-  # jupyterlab is not necessary since we get the source from pypi
pkgs/development/python-modules/jupyterlab-pygments/default.nix-  postPatch = ''
pkgs/development/python-modules/jupyterlab-pygments/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/jupyterlab-pygments/default.nix-      --replace '"jupyterlab>=4.0.0,<5",' ""
pkgs/development/python-modules/jupyterlab-pygments/default.nix-  '';
pkgs/development/python-modules/jupyterlab-pygments/default.nix-
pkgs/development/python-modules/jupyterlab-pygments/default.nix-  nativeBuildInputs = [
pkgs/development/python-modules/jupyterlab-pygments/default.nix-    hatch-jupyter-builder
pkgs/development/python-modules/jupyterlab-pygments/default.nix-    hatch-nodejs-version
pkgs/development/python-modules/jupyterlab-pygments/default.nix-    hatchling
pkgs/development/python-modules/jupyterlab-pygments/default.nix-  ];
pkgs/development/python-modules/jupyterlab-pygments/default.nix-
pkgs/development/python-modules/jupyterlab-pygments/default.nix-  # no tests exist on upstream repo
--
--
pkgs/development/python-modules/pylibjpeg-libjpeg/default.nix-
pkgs/development/python-modules/pylibjpeg-libjpeg/default.nix-    src = fetchFromGitHub {
pkgs/development/python-modules/pylibjpeg-libjpeg/default.nix-      owner = "pydicom";
pkgs/development/python-modules/pylibjpeg-libjpeg/default.nix-      repo = "pylibjpeg-libjpeg";
pkgs/development/python-modules/pylibjpeg-libjpeg/default.nix-      tag = "v${self.version}";
pkgs/development/python-modules/pylibjpeg-libjpeg/default.nix-      hash = "sha256-P01pofPLTOa5ynsCkLnxiMzVfCg4tbT+/CcpPTeSViw=";
pkgs/development/python-modules/pylibjpeg-libjpeg/default.nix-    };
pkgs/development/python-modules/pylibjpeg-libjpeg/default.nix-
pkgs/development/python-modules/pylibjpeg-libjpeg/default.nix-    postPatch = ''
pkgs/development/python-modules/pylibjpeg-libjpeg/default.nix:      substituteInPlace pyproject.toml \
pkgs/development/python-modules/pylibjpeg-libjpeg/default.nix-        --replace-fail 'poetry-core >=1.8,<2' 'poetry-core'
pkgs/development/python-modules/pylibjpeg-libjpeg/default.nix-      rmdir lib/libjpeg
pkgs/development/python-modules/pylibjpeg-libjpeg/default.nix-      cp -r ${libjpeg-tools.src} lib/libjpeg
pkgs/development/python-modules/pylibjpeg-libjpeg/default.nix-      chmod u+w lib/libjpeg
pkgs/development/python-modules/pylibjpeg-libjpeg/default.nix-    '';
pkgs/development/python-modules/pylibjpeg-libjpeg/default.nix-
pkgs/development/python-modules/pylibjpeg-libjpeg/default.nix-    build-system = [
pkgs/development/python-modules/pylibjpeg-libjpeg/default.nix-      cython
pkgs/development/python-modules/pylibjpeg-libjpeg/default.nix-      poetry-core
pkgs/development/python-modules/pylibjpeg-libjpeg/default.nix-      setuptools
--
--
pkgs/development/python-modules/zigpy/default.nix-
pkgs/development/python-modules/zigpy/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/zigpy/default.nix-    owner = "zigpy";
pkgs/development/python-modules/zigpy/default.nix-    repo = "zigpy";
pkgs/development/python-modules/zigpy/default.nix-    tag = version;
pkgs/development/python-modules/zigpy/default.nix-    hash = "sha256-j1gB5+UCseakfkqgA7hmm7qCchIN/BIAAZTdy7mKztM=";
pkgs/development/python-modules/zigpy/default.nix-  };
pkgs/development/python-modules/zigpy/default.nix-
pkgs/development/python-modules/zigpy/default.nix-  postPatch = ''
pkgs/development/python-modules/zigpy/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/zigpy/default.nix-      --replace-fail '"setuptools-git-versioning<2"' "" \
pkgs/development/python-modules/zigpy/default.nix-      --replace-fail 'dynamic = ["version"]' 'version = "${version}"'
pkgs/development/python-modules/zigpy/default.nix-  '';
pkgs/development/python-modules/zigpy/default.nix-
pkgs/development/python-modules/zigpy/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/zigpy/default.nix-
pkgs/development/python-modules/zigpy/default.nix-  dependencies = [
pkgs/development/python-modules/zigpy/default.nix-    attrs
pkgs/development/python-modules/zigpy/default.nix-    aiohttp
pkgs/development/python-modules/zigpy/default.nix-    aiosqlite
--
--
pkgs/development/python-modules/graphql-core/default.nix-
pkgs/development/python-modules/graphql-core/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/graphql-core/default.nix-    owner = "graphql-python";
pkgs/development/python-modules/graphql-core/default.nix-    repo = "graphql-core";
pkgs/development/python-modules/graphql-core/default.nix-    tag = "v${version}";
pkgs/development/python-modules/graphql-core/default.nix-    hash = "sha256-RkVyoTSVmtKhs42IK+oOrOL4uBs3As3N5KY0Sz1VaDQ=";
pkgs/development/python-modules/graphql-core/default.nix-  };
pkgs/development/python-modules/graphql-core/default.nix-
pkgs/development/python-modules/graphql-core/default.nix-  postPatch = ''
pkgs/development/python-modules/graphql-core/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/graphql-core/default.nix-      --replace-fail ', "setuptools>=59,<76"' ""
pkgs/development/python-modules/graphql-core/default.nix-  '';
pkgs/development/python-modules/graphql-core/default.nix-
pkgs/development/python-modules/graphql-core/default.nix-  build-system = [
pkgs/development/python-modules/graphql-core/default.nix-    poetry-core
pkgs/development/python-modules/graphql-core/default.nix-  ];
pkgs/development/python-modules/graphql-core/default.nix-
pkgs/development/python-modules/graphql-core/default.nix-  nativeCheckInputs = [
pkgs/development/python-modules/graphql-core/default.nix-    pytest-asyncio
pkgs/development/python-modules/graphql-core/default.nix-    pytest-benchmark
--
--
pkgs/development/python-modules/matchpy/default.nix-      name = "fix-versioneer-py312.patch";
pkgs/development/python-modules/matchpy/default.nix-      url = "https://github.com/HPAC/matchpy/commit/965d7c39689b9f2473a78ed06b83f2be701e234d.patch";
pkgs/development/python-modules/matchpy/default.nix-      hash = "sha256-xXADCSIhq1ARny2twzrhR1J8LkMFWFl6tmGxrM8RvkU=";
pkgs/development/python-modules/matchpy/default.nix-    })
pkgs/development/python-modules/matchpy/default.nix-  ];
pkgs/development/python-modules/matchpy/default.nix-
pkgs/development/python-modules/matchpy/default.nix-  postPatch = ''
pkgs/development/python-modules/matchpy/default.nix-    sed -i '/pytest-runner/d' setup.cfg
pkgs/development/python-modules/matchpy/default.nix-
pkgs/development/python-modules/matchpy/default.nix:    substituteInPlace setup.cfg \
pkgs/development/python-modules/matchpy/default.nix-      --replace "multiset>=2.0,<3.0" "multiset"
pkgs/development/python-modules/matchpy/default.nix-  '';
pkgs/development/python-modules/matchpy/default.nix-
pkgs/development/python-modules/matchpy/default.nix-  nativeBuildInputs = [ setuptools-scm ];
pkgs/development/python-modules/matchpy/default.nix-
pkgs/development/python-modules/matchpy/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/matchpy/default.nix-    hopcroftkarp
pkgs/development/python-modules/matchpy/default.nix-    multiset
pkgs/development/python-modules/matchpy/default.nix-  ];
pkgs/development/python-modules/matchpy/default.nix-
--
--
pkgs/development/python-modules/psycopg/default.nix-    format = "pyproject";
pkgs/development/python-modules/psycopg/default.nix-
pkgs/development/python-modules/psycopg/default.nix-    # apply patches to base repo
pkgs/development/python-modules/psycopg/default.nix-    inherit patches;
pkgs/development/python-modules/psycopg/default.nix-
pkgs/development/python-modules/psycopg/default.nix-    # move into source root after patching
pkgs/development/python-modules/psycopg/default.nix-    postPatch = ''
pkgs/development/python-modules/psycopg/default.nix-      cd psycopg_c
pkgs/development/python-modules/psycopg/default.nix-
pkgs/development/python-modules/psycopg/default.nix:      substituteInPlace pyproject.toml \
pkgs/development/python-modules/psycopg/default.nix-        --replace-fail "Cython >= 3.0.0, < 3.1.0" "Cython"
pkgs/development/python-modules/psycopg/default.nix-    '';
pkgs/development/python-modules/psycopg/default.nix-
pkgs/development/python-modules/psycopg/default.nix-    nativeBuildInputs = [
pkgs/development/python-modules/psycopg/default.nix-      cython
pkgs/development/python-modules/psycopg/default.nix-      libpq.pg_config
pkgs/development/python-modules/psycopg/default.nix-      setuptools
pkgs/development/python-modules/psycopg/default.nix-      tomli
pkgs/development/python-modules/psycopg/default.nix-    ];
pkgs/development/python-modules/psycopg/default.nix-
--
--
pkgs/development/python-modules/pydemumble/default.nix-    owner = "angr";
pkgs/development/python-modules/pydemumble/default.nix-    repo = "pydemumble";
pkgs/development/python-modules/pydemumble/default.nix-    tag = "v${version}";
pkgs/development/python-modules/pydemumble/default.nix-    hash = "sha256-JAUMTOYGHu64L0zLK2dzf0poHrGGiE29WoAR5kRsR+s=";
pkgs/development/python-modules/pydemumble/default.nix-    fetchSubmodules = true;
pkgs/development/python-modules/pydemumble/default.nix-  };
pkgs/development/python-modules/pydemumble/default.nix-
pkgs/development/python-modules/pydemumble/default.nix-  postPatch = ''
pkgs/development/python-modules/pydemumble/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/pydemumble/default.nix-      --replace-fail \
pkgs/development/python-modules/pydemumble/default.nix-        ', "nanobind >=1.3.2"' \
pkgs/development/python-modules/pydemumble/default.nix-        ""
pkgs/development/python-modules/pydemumble/default.nix-  '';
pkgs/development/python-modules/pydemumble/default.nix-
pkgs/development/python-modules/pydemumble/default.nix-  build-system = [
pkgs/development/python-modules/pydemumble/default.nix-    scikit-build-core
pkgs/development/python-modules/pydemumble/default.nix-  ];
pkgs/development/python-modules/pydemumble/default.nix-
pkgs/development/python-modules/pydemumble/default.nix-  dontUseCmakeConfigure = true;
--
pkgs/development/python-modules/nicegui-highcharts/default.nix-  pyproject = true;
pkgs/development/python-modules/nicegui-highcharts/default.nix-
pkgs/development/python-modules/nicegui-highcharts/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/nicegui-highcharts/default.nix-    owner = "zauberzeug";
pkgs/development/python-modules/nicegui-highcharts/default.nix-    repo = "nicegui-highcharts";
pkgs/development/python-modules/nicegui-highcharts/default.nix-    tag = "v${version}";
pkgs/development/python-modules/nicegui-highcharts/default.nix-    hash = "sha256-9COui3gqLZqJSeZyzazxQcOc2oM9Li+dLBoy5VcEKBw=";
pkgs/development/python-modules/nicegui-highcharts/default.nix-  };
pkgs/development/python-modules/nicegui-highcharts/default.nix-
pkgs/development/python-modules/nicegui-highcharts/default.nix-  postPatch = ''
pkgs/development/python-modules/nicegui-highcharts/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/nicegui-highcharts/default.nix-      --replace-fail "setuptools>=30.3.0,<50" "setuptools"
pkgs/development/python-modules/nicegui-highcharts/default.nix-  '';
pkgs/development/python-modules/nicegui-highcharts/default.nix-
pkgs/development/python-modules/nicegui-highcharts/default.nix-  pythonRelaxDeps = [
pkgs/development/python-modules/nicegui-highcharts/default.nix-    "docutils"
pkgs/development/python-modules/nicegui-highcharts/default.nix-    "nicegui"
pkgs/development/python-modules/nicegui-highcharts/default.nix-  ];
pkgs/development/python-modules/nicegui-highcharts/default.nix-
pkgs/development/python-modules/nicegui-highcharts/default.nix-  build-system = [
pkgs/development/python-modules/nicegui-highcharts/default.nix-    poetry-core
--
--
pkgs/development/python-modules/scipy/default.nix-  # perform this substitution even though python3.pkgs.numpy is of version 2
pkgs/development/python-modules/scipy/default.nix-  # nowadays, because our ecosystem unfortunately doesn't allow easily
pkgs/development/python-modules/scipy/default.nix-  # separating runtime and build-system dependencies. See also:
pkgs/development/python-modules/scipy/default.nix-  #
pkgs/development/python-modules/scipy/default.nix-  # https://discourse.nixos.org/t/several-comments-about-priorities-and-new-policies-in-the-python-ecosystem/51790
pkgs/development/python-modules/scipy/default.nix-  #
pkgs/development/python-modules/scipy/default.nix-  # Being able to build (& run) with Numpy 1 helps for python environments
pkgs/development/python-modules/scipy/default.nix-  # that override globally the `numpy` attribute to point to `numpy_1`.
pkgs/development/python-modules/scipy/default.nix-  postPatch = ''
pkgs/development/python-modules/scipy/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/scipy/default.nix-      --replace-fail "numpy>=2.0.0,<2.6" numpy
pkgs/development/python-modules/scipy/default.nix-  '';
pkgs/development/python-modules/scipy/default.nix-
pkgs/development/python-modules/scipy/default.nix-  build-system = [
pkgs/development/python-modules/scipy/default.nix-    cython
pkgs/development/python-modules/scipy/default.nix-    gfortran
pkgs/development/python-modules/scipy/default.nix-    meson-python
pkgs/development/python-modules/scipy/default.nix-    nukeReferences
pkgs/development/python-modules/scipy/default.nix-    pythran
pkgs/development/python-modules/scipy/default.nix-    pkg-config
--
--
pkgs/development/python-modules/tree-sitter-language-pack/default.nix-    pname = "tree_sitter_language_pack";
pkgs/development/python-modules/tree-sitter-language-pack/default.nix-    inherit version;
pkgs/development/python-modules/tree-sitter-language-pack/default.nix-    hash = "sha256-kA6zvYLBvPXPIO2FKxtv3H6uieQKhg+l4iGnlmh8NZo=";
pkgs/development/python-modules/tree-sitter-language-pack/default.nix-  };
pkgs/development/python-modules/tree-sitter-language-pack/default.nix-
pkgs/development/python-modules/tree-sitter-language-pack/default.nix-  # Upstream bumped the setuptools and typing-extensions dependencies, but we can still use older versions
pkgs/development/python-modules/tree-sitter-language-pack/default.nix-  # since the newer ones aren’t packaged in nixpkgs. We can't use pythonRelaxDepsHook here because it runs
pkgs/development/python-modules/tree-sitter-language-pack/default.nix-  # in postBuild, while the dependency check occurs during the build phase.
pkgs/development/python-modules/tree-sitter-language-pack/default.nix-  postPatch = ''
pkgs/development/python-modules/tree-sitter-language-pack/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/tree-sitter-language-pack/default.nix-      --replace-fail "setuptools>=80.9.0" "setuptools>=78.1.0" \
pkgs/development/python-modules/tree-sitter-language-pack/default.nix-      --replace-fail "typing-extensions>=4.14.0" "typing-extensions>=4.13.2"
pkgs/development/python-modules/tree-sitter-language-pack/default.nix-  '';
pkgs/development/python-modules/tree-sitter-language-pack/default.nix-
pkgs/development/python-modules/tree-sitter-language-pack/default.nix-  build-system = [
pkgs/development/python-modules/tree-sitter-language-pack/default.nix-    cython
pkgs/development/python-modules/tree-sitter-language-pack/default.nix-    setuptools
pkgs/development/python-modules/tree-sitter-language-pack/default.nix-    typing-extensions
pkgs/development/python-modules/tree-sitter-language-pack/default.nix-  ];
pkgs/development/python-modules/tree-sitter-language-pack/default.nix-
--
pkgs/development/python-modules/moderngl/default.nix-  pyproject = true;
--
pkgs/development/python-modules/unidic/default.nix-    owner = "polm";
pkgs/development/python-modules/unidic/default.nix-    repo = "unidic-py";
pkgs/development/python-modules/unidic/default.nix-    tag = "v${version}";
pkgs/development/python-modules/unidic/default.nix-    hash = "sha256-srhQDXGgoIMhYuCbyQB3kF4LrODnoOqLbjBQMvhPieY=";
pkgs/development/python-modules/unidic/default.nix-  };
pkgs/development/python-modules/unidic/default.nix-
pkgs/development/python-modules/unidic/default.nix-  patches = [ ./fix-download-directory.patch ];
pkgs/development/python-modules/unidic/default.nix-
pkgs/development/python-modules/unidic/default.nix-  postPatch = ''
pkgs/development/python-modules/unidic/default.nix:    substituteInPlace setup.cfg \
pkgs/development/python-modules/unidic/default.nix-      --replace "wasabi>=0.6.0,<1.0.0" "wasabi"
pkgs/development/python-modules/unidic/default.nix-  '';
pkgs/development/python-modules/unidic/default.nix-
pkgs/development/python-modules/unidic/default.nix-  # no tests
pkgs/development/python-modules/unidic/default.nix-  doCheck = false;
pkgs/development/python-modules/unidic/default.nix-
pkgs/development/python-modules/unidic/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/unidic/default.nix-    requests
pkgs/development/python-modules/unidic/default.nix-    tqdm
pkgs/development/python-modules/unidic/default.nix-    wasabi
--
--
pkgs/development/python-modules/zope-i18nmessageid/default.nix-
pkgs/development/python-modules/zope-i18nmessageid/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/zope-i18nmessageid/default.nix-    owner = "zopefoundation";
pkgs/development/python-modules/zope-i18nmessageid/default.nix-    repo = "zope.i18nmessageid";
pkgs/development/python-modules/zope-i18nmessageid/default.nix-    tag = version;
pkgs/development/python-modules/zope-i18nmessageid/default.nix-    hash = "sha256-rdTs1pNMKpPAR2CewXdg1KmI61Sw5r62OobYlJHsUaQ=";
pkgs/development/python-modules/zope-i18nmessageid/default.nix-  };
pkgs/development/python-modules/zope-i18nmessageid/default.nix-
pkgs/development/python-modules/zope-i18nmessageid/default.nix-  postPatch = ''
pkgs/development/python-modules/zope-i18nmessageid/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/zope-i18nmessageid/default.nix-      --replace-fail "setuptools<74" "setuptools"
pkgs/development/python-modules/zope-i18nmessageid/default.nix-  '';
pkgs/development/python-modules/zope-i18nmessageid/default.nix-
pkgs/development/python-modules/zope-i18nmessageid/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/zope-i18nmessageid/default.nix-
pkgs/development/python-modules/zope-i18nmessageid/default.nix-  nativeCheckInputs = [
pkgs/development/python-modules/zope-i18nmessageid/default.nix-    unittestCheckHook
pkgs/development/python-modules/zope-i18nmessageid/default.nix-    zope-testrunner
pkgs/development/python-modules/zope-i18nmessageid/default.nix-  ];
pkgs/development/python-modules/zope-i18nmessageid/default.nix-
--
--
pkgs/development/python-modules/vsts/default.nix-  pname = "vsts";
pkgs/development/python-modules/vsts/default.nix-
pkgs/development/python-modules/vsts/default.nix-  src = fetchPypi {
pkgs/development/python-modules/vsts/default.nix-    inherit pname version;
pkgs/development/python-modules/vsts/default.nix-    sha256 = "15sgwqa72ynpahj101r2kc15s3dnsafg5gqx0sz3hnqz29h925ys";
pkgs/development/python-modules/vsts/default.nix-  };
pkgs/development/python-modules/vsts/default.nix-
pkgs/development/python-modules/vsts/default.nix-  propagatedBuildInputs = [ msrest ];
pkgs/development/python-modules/vsts/default.nix-
pkgs/development/python-modules/vsts/default.nix-  postPatch = ''
pkgs/development/python-modules/vsts/default.nix:    substituteInPlace setup.py --replace "msrest>=0.6.0,<0.7.0" "msrest"
pkgs/development/python-modules/vsts/default.nix-  '';
pkgs/development/python-modules/vsts/default.nix-
pkgs/development/python-modules/vsts/default.nix-  # Tests are highly impure
pkgs/development/python-modules/vsts/default.nix-  checkPhase = ''
pkgs/development/python-modules/vsts/default.nix-    ${python.interpreter} -c 'import vsts.version; print(vsts.version.VERSION)'
pkgs/development/python-modules/vsts/default.nix-  '';
pkgs/development/python-modules/vsts/default.nix-
pkgs/development/python-modules/vsts/default.nix-  meta = with lib; {
pkgs/development/python-modules/vsts/default.nix-    description = "Python APIs for interacting with and managing Azure DevOps";
pkgs/development/python-modules/vsts/default.nix-    homepage = "https://github.com/microsoft/azure-devops-python-api";
--
pkgs/development/python-modules/extractcode/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/extractcode/default.nix-    owner = "aboutcode-org";
pkgs/development/python-modules/extractcode/default.nix-    repo = "extractcode";
pkgs/development/python-modules/extractcode/default.nix-    tag = "v${version}";
pkgs/development/python-modules/extractcode/default.nix-    hash = "sha256-mPHGe/pMaOnIykDd4AjGcvh/T4UrbaGxrSVGhchqYFM=";
pkgs/development/python-modules/extractcode/default.nix-  };
pkgs/development/python-modules/extractcode/default.nix-
pkgs/development/python-modules/extractcode/default.nix-  postPatch = ''
pkgs/development/python-modules/extractcode/default.nix-    # PEP440 support was removed in newer setuptools, https://github.com/nexB/extractcode/pull/46
pkgs/development/python-modules/extractcode/default.nix:    substituteInPlace setup.cfg \
pkgs/development/python-modules/extractcode/default.nix-      --replace-fail ">=3.6.*" ">=3.6"
pkgs/development/python-modules/extractcode/default.nix-  '';
pkgs/development/python-modules/extractcode/default.nix-
pkgs/development/python-modules/extractcode/default.nix-  dontConfigure = true;
pkgs/development/python-modules/extractcode/default.nix-
pkgs/development/python-modules/extractcode/default.nix-  build-system = [ setuptools-scm ];
pkgs/development/python-modules/extractcode/default.nix-
pkgs/development/python-modules/extractcode/default.nix-  dependencies = [
pkgs/development/python-modules/extractcode/default.nix-    extractcode-7z
pkgs/development/python-modules/extractcode/default.nix-    extractcode-libarchive
--
--
pkgs/development/python-modules/telfhash/default.nix-    repo = "telfhash";
pkgs/development/python-modules/telfhash/default.nix-    rev = "v${version}";
pkgs/development/python-modules/telfhash/default.nix-    sha256 = "124zajv43wx9l8rvdvmzcnbh0xpzmbn253pznpbjwvygfx16gq02";
pkgs/development/python-modules/telfhash/default.nix-  };
pkgs/development/python-modules/telfhash/default.nix-
pkgs/development/python-modules/telfhash/default.nix-  # The tlsh library's name is just "tlsh"
pkgs/development/python-modules/telfhash/default.nix-  postPatch = ''
pkgs/development/python-modules/telfhash/default.nix:    substituteInPlace requirements.txt \
pkgs/development/python-modules/telfhash/default.nix-       --replace-fail "python-tlsh" "tlsh" \
pkgs/development/python-modules/telfhash/default.nix-       --replace-fail "py-tlsh" "tlsh" \
pkgs/development/python-modules/telfhash/default.nix-       --replace-fail "nose>=1.3.7" ""
pkgs/development/python-modules/telfhash/default.nix-  '';
pkgs/development/python-modules/telfhash/default.nix-
pkgs/development/python-modules/telfhash/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/telfhash/default.nix-
pkgs/development/python-modules/telfhash/default.nix-  dependencies = [
pkgs/development/python-modules/telfhash/default.nix-    capstone
pkgs/development/python-modules/telfhash/default.nix-    pyelftools
--
pkgs/development/python-modules/h5py/default.nix-    inherit pname version;
pkgs/development/python-modules/h5py/default.nix-    hash = "sha256-I3IRay4NXT5ecFt/Zj98jZb6eaQFLSUEhO+R0k1qCPQ=";
pkgs/development/python-modules/h5py/default.nix-  };
pkgs/development/python-modules/h5py/default.nix-
pkgs/development/python-modules/h5py/default.nix-  pythonRelaxDeps = [ "mpi4py" ];
pkgs/development/python-modules/h5py/default.nix-
pkgs/development/python-modules/h5py/default.nix-  # Avoid strict pinning of Numpy, can't be replaced with pythonRelaxDepsHook,
pkgs/development/python-modules/h5py/default.nix-  # as these are build time dependencies. See:
pkgs/development/python-modules/h5py/default.nix-  # https://github.com/NixOS/nixpkgs/issues/327941
pkgs/development/python-modules/h5py/default.nix-  postPatch = ''
pkgs/development/python-modules/h5py/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/h5py/default.nix-      --replace-fail "numpy >=2.0.0, <3" "numpy"
pkgs/development/python-modules/h5py/default.nix-  '';
pkgs/development/python-modules/h5py/default.nix-
pkgs/development/python-modules/h5py/default.nix-  env = {
pkgs/development/python-modules/h5py/default.nix-    HDF5_DIR = "${hdf5}";
pkgs/development/python-modules/h5py/default.nix-    HDF5_MPI = if mpiSupport then "ON" else "OFF";
pkgs/development/python-modules/h5py/default.nix-    # See discussion at https://github.com/h5py/h5py/issues/2560
pkgs/development/python-modules/h5py/default.nix-    H5PY_SETUP_REQUIRES = 0;
pkgs/development/python-modules/h5py/default.nix-  };
pkgs/development/python-modules/h5py/default.nix-
--
--
pkgs/development/python-modules/annoy/default.nix-
pkgs/development/python-modules/annoy/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/annoy/default.nix-    owner = "spotify";
pkgs/development/python-modules/annoy/default.nix-    repo = "annoy";
pkgs/development/python-modules/annoy/default.nix-    tag = "v${version}";
pkgs/development/python-modules/annoy/default.nix-    hash = "sha256-oJHW4lULRun2in35pBGOKg44s5kgLH2BKiMOzVu4rf4=";
pkgs/development/python-modules/annoy/default.nix-  };
pkgs/development/python-modules/annoy/default.nix-
pkgs/development/python-modules/annoy/default.nix-  postPatch = ''
pkgs/development/python-modules/annoy/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/annoy/default.nix-      --replace-fail "'nose>=1.0'" ""
pkgs/development/python-modules/annoy/default.nix-  '';
pkgs/development/python-modules/annoy/default.nix-
pkgs/development/python-modules/annoy/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/annoy/default.nix-
pkgs/development/python-modules/annoy/default.nix-  nativeBuildInputs = [ h5py ];
pkgs/development/python-modules/annoy/default.nix-
pkgs/development/python-modules/annoy/default.nix-  nativeCheckInputs = [
pkgs/development/python-modules/annoy/default.nix-    numpy
pkgs/development/python-modules/annoy/default.nix-    pytestCheckHook
--
--
pkgs/development/python-modules/openevsewifi/default.nix-
pkgs/development/python-modules/openevsewifi/default.nix-  pythonImportsCheck = [ "openevsewifi" ];
pkgs/development/python-modules/openevsewifi/default.nix-
pkgs/development/python-modules/openevsewifi/default.nix-  meta = with lib; {
pkgs/development/python-modules/openevsewifi/default.nix-    description = "Module for communicating with the wifi module from OpenEVSE";
pkgs/development/python-modules/openevsewifi/default.nix-    homepage = "https://github.com/miniconfig/python-openevse-wifi";
pkgs/development/python-modules/openevsewifi/default.nix-    license = with licenses; [ mit ];
pkgs/development/python-modules/openevsewifi/default.nix-    maintainers = with maintainers; [ fab ];
--
pkgs/development/python-modules/flask-limiter/default.nix-  patches = [
pkgs/development/python-modules/flask-limiter/default.nix-    # permit use of rich < 15 -- remove when updating past 3.12
pkgs/development/python-modules/flask-limiter/default.nix-    (fetchpatch {
pkgs/development/python-modules/flask-limiter/default.nix-      url = "https://github.com/alisaifee/flask-limiter/commit/008a5c89f249e18e5375f16d79efc3ac518e9bcc.patch";
pkgs/development/python-modules/flask-limiter/default.nix-      hash = "sha256-dvTPVnuPs7xCRfUBBA1bgeWGuevFUZ+Kgl9MBHdgfKU=";
pkgs/development/python-modules/flask-limiter/default.nix-    })
pkgs/development/python-modules/flask-limiter/default.nix-  ];
pkgs/development/python-modules/flask-limiter/default.nix-
pkgs/development/python-modules/flask-limiter/default.nix-  postPatch = ''
pkgs/development/python-modules/flask-limiter/default.nix-    # flask-restful is unmaintained and breaks regularly, don't depend on it
pkgs/development/python-modules/flask-limiter/default.nix:    substituteInPlace tests/test_views.py \
pkgs/development/python-modules/flask-limiter/default.nix-      --replace-fail "import flask_restful" ""
--
pkgs/development/python-modules/orange3/default.nix-      hash = "sha256-P2e3Wq33UXnTmGSxkoW8kYYCBfYBB9Z50v4g7n//Fbw=";
pkgs/development/python-modules/orange3/default.nix-    };
pkgs/development/python-modules/orange3/default.nix-
pkgs/development/python-modules/orange3/default.nix-    build-system = [
pkgs/development/python-modules/orange3/default.nix-      oldest-supported-numpy
pkgs/development/python-modules/orange3/default.nix-      setuptools
pkgs/development/python-modules/orange3/default.nix-    ];
pkgs/development/python-modules/orange3/default.nix-
pkgs/development/python-modules/orange3/default.nix-    postPatch = ''
pkgs/development/python-modules/orange3/default.nix:      substituteInPlace pyproject.toml \
pkgs/development/python-modules/orange3/default.nix-          --replace-fail 'cython>=3.0' 'cython'
pkgs/development/python-modules/orange3/default.nix-
pkgs/development/python-modules/orange3/default.nix-      # disable update checking
pkgs/development/python-modules/orange3/default.nix-      echo -e "def check_for_updates():\n\tpass" >> Orange/canvas/__main__.py
pkgs/development/python-modules/orange3/default.nix-    '';
pkgs/development/python-modules/orange3/default.nix-
pkgs/development/python-modules/orange3/default.nix-    nativeBuildInputs = [
pkgs/development/python-modules/orange3/default.nix-      copyDesktopItems
pkgs/development/python-modules/orange3/default.nix-      cython
pkgs/development/python-modules/orange3/default.nix-      qt5.wrapQtAppsHook
--
pkgs/development/python-modules/orange3/default.nix-        preCheck = ''
pkgs/development/python-modules/orange3/default.nix-          export HOME=$(mktemp -d)
pkgs/development/python-modules/orange3/default.nix-          export QT_PLUGIN_PATH="${qt5.qtbase.bin}/${qt5.qtbase.qtPluginPrefix}"
--
pkgs/development/python-modules/pydmd/default.nix-
pkgs/development/python-modules/pydmd/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/pydmd/default.nix-    owner = "PyDMD";
pkgs/development/python-modules/pydmd/default.nix-    repo = "PyDMD";
pkgs/development/python-modules/pydmd/default.nix-    tag = version;
pkgs/development/python-modules/pydmd/default.nix-    hash = "sha256-u8dW90FZSZaVbPNeILeZyOwAU0WOAeTAMCHpe7n4Bi4=";
pkgs/development/python-modules/pydmd/default.nix-  };
pkgs/development/python-modules/pydmd/default.nix-
pkgs/development/python-modules/pydmd/default.nix-  postPatch = ''
pkgs/development/python-modules/pydmd/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/pydmd/default.nix-      --replace-fail "setuptools-git-versioning>=2.0,<3" "setuptools-git-versioning"
pkgs/development/python-modules/pydmd/default.nix-  '';
pkgs/development/python-modules/pydmd/default.nix-
pkgs/development/python-modules/pydmd/default.nix-  build-system = [
pkgs/development/python-modules/pydmd/default.nix-    setuptools
pkgs/development/python-modules/pydmd/default.nix-    setuptools-git-versioning
pkgs/development/python-modules/pydmd/default.nix-  ];
pkgs/development/python-modules/pydmd/default.nix-
pkgs/development/python-modules/pydmd/default.nix-  dependencies = [
pkgs/development/python-modules/pydmd/default.nix-    ezyrb
--
--
pkgs/development/python-modules/dipy/default.nix-
pkgs/development/python-modules/dipy/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/dipy/default.nix-    owner = "dipy";
pkgs/development/python-modules/dipy/default.nix-    repo = "dipy";
pkgs/development/python-modules/dipy/default.nix-    tag = version;
pkgs/development/python-modules/dipy/default.nix-    hash = "sha256-6cpxuk2PL43kjQ+6UGiUHUXC7pC9OlW9kZvGOdEXyzw=";
pkgs/development/python-modules/dipy/default.nix-  };
pkgs/development/python-modules/dipy/default.nix-
pkgs/development/python-modules/dipy/default.nix-  postPatch = ''
pkgs/development/python-modules/dipy/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/dipy/default.nix-      --replace-fail "numpy==" "numpy>="
pkgs/development/python-modules/dipy/default.nix-  '';
pkgs/development/python-modules/dipy/default.nix-
pkgs/development/python-modules/dipy/default.nix-  build-system = [
pkgs/development/python-modules/dipy/default.nix-    cython
pkgs/development/python-modules/dipy/default.nix-    meson-python
pkgs/development/python-modules/dipy/default.nix-    numpy
pkgs/development/python-modules/dipy/default.nix-    packaging
pkgs/development/python-modules/dipy/default.nix-  ];
pkgs/development/python-modules/dipy/default.nix-
--
--
pkgs/development/python-modules/devolo-plc-api/default.nix-
pkgs/development/python-modules/devolo-plc-api/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/devolo-plc-api/default.nix-    owner = "2Fake";
pkgs/development/python-modules/devolo-plc-api/default.nix-    repo = "devolo_plc_api";
pkgs/development/python-modules/devolo-plc-api/default.nix-    tag = "v${version}";
pkgs/development/python-modules/devolo-plc-api/default.nix-    hash = "sha256-bmZcjvqZwVJzDsdtSbQvJpry2QSSuB6/jOTWG1+jyV4=";
pkgs/development/python-modules/devolo-plc-api/default.nix-  };
pkgs/development/python-modules/devolo-plc-api/default.nix-
pkgs/development/python-modules/devolo-plc-api/default.nix-  postPatch = ''
pkgs/development/python-modules/devolo-plc-api/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/devolo-plc-api/default.nix-      --replace-fail "protobuf>=4.22.0" "protobuf"
pkgs/development/python-modules/devolo-plc-api/default.nix-  '';
pkgs/development/python-modules/devolo-plc-api/default.nix-
pkgs/development/python-modules/devolo-plc-api/default.nix-  build-system = [ setuptools-scm ];
pkgs/development/python-modules/devolo-plc-api/default.nix-
pkgs/development/python-modules/devolo-plc-api/default.nix-  dependencies = [
pkgs/development/python-modules/devolo-plc-api/default.nix-    httpx
pkgs/development/python-modules/devolo-plc-api/default.nix-    protobuf
pkgs/development/python-modules/devolo-plc-api/default.nix-    segno
pkgs/development/python-modules/devolo-plc-api/default.nix-    tenacity
--
--
pkgs/development/python-modules/click-configfile/default.nix-
pkgs/development/python-modules/click-configfile/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/click-configfile/default.nix-    click
pkgs/development/python-modules/click-configfile/default.nix-    six
pkgs/development/python-modules/click-configfile/default.nix-  ];
pkgs/development/python-modules/click-configfile/default.nix-
pkgs/development/python-modules/click-configfile/default.nix-  nativeCheckInputs = [ pytestCheckHook ];
pkgs/development/python-modules/click-configfile/default.nix-
pkgs/development/python-modules/click-configfile/default.nix-  postPatch = ''
pkgs/development/python-modules/click-configfile/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/click-configfile/default.nix-      --replace "install_requires=install_requires," 'install_requires=["click >= 6.6", "six >= 1.10"],'
pkgs/development/python-modules/click-configfile/default.nix-  '';
pkgs/development/python-modules/click-configfile/default.nix-
pkgs/development/python-modules/click-configfile/default.nix-  pythonImportsCheck = [ "click_configfile" ];
pkgs/development/python-modules/click-configfile/default.nix-
pkgs/development/python-modules/click-configfile/default.nix-  disabledTests = [
pkgs/development/python-modules/click-configfile/default.nix-    "test_configfile__with_unbound_section"
pkgs/development/python-modules/click-configfile/default.nix-    "test_matches_section__with_bad_arg"
pkgs/development/python-modules/click-configfile/default.nix-  ];
pkgs/development/python-modules/click-configfile/default.nix-
--
--
pkgs/development/python-modules/rmcl/default.nix-
pkgs/development/python-modules/rmcl/default.nix-  format = "pyproject";
pkgs/development/python-modules/rmcl/default.nix-
pkgs/development/python-modules/rmcl/default.nix-  src = fetchPypi {
pkgs/development/python-modules/rmcl/default.nix-    inherit pname version;
pkgs/development/python-modules/rmcl/default.nix-    sha256 = "58de4758e7e3cb7acbf28fcfa80f4155252afdfb191beb4ba4aa36961f66cc67";
pkgs/development/python-modules/rmcl/default.nix-  };
pkgs/development/python-modules/rmcl/default.nix-
pkgs/development/python-modules/rmcl/default.nix-  postPatch = ''
pkgs/development/python-modules/rmcl/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/rmcl/default.nix-      --replace '= "^' '= ">='
pkgs/development/python-modules/rmcl/default.nix-  '';
pkgs/development/python-modules/rmcl/default.nix-
pkgs/development/python-modules/rmcl/default.nix-  nativeBuildInputs = [ poetry-core ];
pkgs/development/python-modules/rmcl/default.nix-
pkgs/development/python-modules/rmcl/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/rmcl/default.nix-    asks
pkgs/development/python-modules/rmcl/default.nix-    trio
pkgs/development/python-modules/rmcl/default.nix-    xdg
pkgs/development/python-modules/rmcl/default.nix-  ];
--
--
pkgs/development/python-modules/amaranth/default.nix-
pkgs/development/python-modules/amaranth/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/amaranth/default.nix-    owner = "amaranth-lang";
pkgs/development/python-modules/amaranth/default.nix-    repo = "amaranth";
pkgs/development/python-modules/amaranth/default.nix-    tag = "v${version}";
pkgs/development/python-modules/amaranth/default.nix-    hash = "sha256-E/PJrvBmlS39KgzDz9sArq4BXwk/JmIMtdxL7MdrWlc=";
pkgs/development/python-modules/amaranth/default.nix-  };
pkgs/development/python-modules/amaranth/default.nix-
pkgs/development/python-modules/amaranth/default.nix-  postPatch = ''
pkgs/development/python-modules/amaranth/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/amaranth/default.nix-      --replace-fail "pdm-backend~=2.3.0" "pdm-backend>=2.3.0"
pkgs/development/python-modules/amaranth/default.nix-  '';
pkgs/development/python-modules/amaranth/default.nix-
pkgs/development/python-modules/amaranth/default.nix-  nativeBuildInputs = [ git ];
pkgs/development/python-modules/amaranth/default.nix-
pkgs/development/python-modules/amaranth/default.nix-  build-system = [ pdm-backend ];
pkgs/development/python-modules/amaranth/default.nix-
pkgs/development/python-modules/amaranth/default.nix-  dependencies = [
pkgs/development/python-modules/amaranth/default.nix-    jschon
pkgs/development/python-modules/amaranth/default.nix-    jinja2
--
--
pkgs/development/python-modules/flask-compress/default.nix-
pkgs/development/python-modules/flask-compress/default.nix-  nativeCheckInputs = [
pkgs/development/python-modules/flask-compress/default.nix-    pytestCheckHook
pkgs/development/python-modules/flask-compress/default.nix-    flask-caching
pkgs/development/python-modules/flask-compress/default.nix-  ];
pkgs/development/python-modules/flask-compress/default.nix-
pkgs/development/python-modules/flask-compress/default.nix-  pythonImportsCheck = [ "flask_compress" ];
pkgs/development/python-modules/flask-compress/default.nix-
pkgs/development/python-modules/flask-compress/default.nix-  postPatch = ''
pkgs/development/python-modules/flask-compress/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/flask-compress/default.nix-      --replace-fail "setuptools_scm[toml]<8" "setuptools_scm"
pkgs/development/python-modules/flask-compress/default.nix-  '';
pkgs/development/python-modules/flask-compress/default.nix-
pkgs/development/python-modules/flask-compress/default.nix-  meta = {
pkgs/development/python-modules/flask-compress/default.nix-    description = "Compress responses in your Flask app with gzip, deflate or brotli";
pkgs/development/python-modules/flask-compress/default.nix-    homepage = "https://github.com/colour-science/flask-compress";
pkgs/development/python-modules/flask-compress/default.nix-    changelog = "https://github.com/colour-science/flask-compress/blob/v${version}/CHANGELOG.md";
pkgs/development/python-modules/flask-compress/default.nix-    license = lib.licenses.mit;
pkgs/development/python-modules/flask-compress/default.nix-    maintainers = with lib.maintainers; [ nickcao ];
pkgs/development/python-modules/flask-compress/default.nix-  };
--
--
pkgs/development/python-modules/numba/default.nix-
pkgs/development/python-modules/numba/default.nix-  postPatch = ''
pkgs/development/python-modules/numba/default.nix:    substituteInPlace numba/cuda/cudadrv/driver.py \
pkgs/development/python-modules/numba/default.nix-      --replace-fail \
pkgs/development/python-modules/numba/default.nix-        "dldir = [" \
pkgs/development/python-modules/numba/default.nix-        "dldir = [ '${addDriverRunpath.driverLink}/lib', "
pkgs/development/python-modules/numba/default.nix-
pkgs/development/python-modules/numba/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/numba/default.nix-      --replace-fail 'max_numpy_run_version = "2.3"' 'max_numpy_run_version = "2.4"'
pkgs/development/python-modules/numba/default.nix:    substituteInPlace numba/__init__.py \
pkgs/development/python-modules/numba/default.nix-      --replace-fail "numpy_version > (2, 2)" "numpy_version > (2, 3)"
pkgs/development/python-modules/numba/default.nix-  '';
pkgs/development/python-modules/numba/default.nix-
pkgs/development/python-modules/numba/default.nix-  env.NIX_CFLAGS_COMPILE = lib.optionalString stdenv.hostPlatform.isDarwin "-I${lib.getInclude stdenv.cc.libcxx}/include/c++/v1";
pkgs/development/python-modules/numba/default.nix-
pkgs/development/python-modules/numba/default.nix-  build-system = [
pkgs/development/python-modules/numba/default.nix-    setuptools
pkgs/development/python-modules/numba/default.nix-    numpy
pkgs/development/python-modules/numba/default.nix-  ];
pkgs/development/python-modules/numba/default.nix-
--
--
pkgs/development/python-modules/zigpy-deconz/default.nix-
pkgs/development/python-modules/zigpy-deconz/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/zigpy-deconz/default.nix-    owner = "zigpy";
pkgs/development/python-modules/zigpy-deconz/default.nix-    repo = "zigpy-deconz";
pkgs/development/python-modules/zigpy-deconz/default.nix-    tag = version;
pkgs/development/python-modules/zigpy-deconz/default.nix-    hash = "sha256-Vw6unTB4PkjlrsXmsry1OC/NMAcd/sCbJ/A/eHgu3JU=";
pkgs/development/python-modules/zigpy-deconz/default.nix-  };
pkgs/development/python-modules/zigpy-deconz/default.nix-
pkgs/development/python-modules/zigpy-deconz/default.nix-  postPatch = ''
pkgs/development/python-modules/zigpy-deconz/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/zigpy-deconz/default.nix-      --replace-fail ', "setuptools-git-versioning<2"' "" \
pkgs/development/python-modules/zigpy-deconz/default.nix-      --replace-fail 'dynamic = ["version"]' 'version = "${version}"'
pkgs/development/python-modules/zigpy-deconz/default.nix-  '';
pkgs/development/python-modules/zigpy-deconz/default.nix-
pkgs/development/python-modules/zigpy-deconz/default.nix-  nativeBuildInputs = [ setuptools ];
pkgs/development/python-modules/zigpy-deconz/default.nix-
pkgs/development/python-modules/zigpy-deconz/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/zigpy-deconz/default.nix-    pyserial
pkgs/development/python-modules/zigpy-deconz/default.nix-    pyserial-asyncio
pkgs/development/python-modules/zigpy-deconz/default.nix-    zigpy
--
--
pkgs/development/python-modules/pmdarima/default.nix-
pkgs/development/python-modules/pmdarima/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/pmdarima/default.nix-    owner = "alkaline-ml";
pkgs/development/python-modules/pmdarima/default.nix-    repo = "pmdarima";
pkgs/development/python-modules/pmdarima/default.nix-    tag = "v${version}";
pkgs/development/python-modules/pmdarima/default.nix-    hash = "sha256-LHwPgQRB/vP3hBM8nqafoCrN3ZSRIMWLzqTqDOETOEc=";
pkgs/development/python-modules/pmdarima/default.nix-  };
pkgs/development/python-modules/pmdarima/default.nix-
pkgs/development/python-modules/pmdarima/default.nix-  postPatch = ''
pkgs/development/python-modules/pmdarima/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/pmdarima/default.nix-      --replace-fail "numpy==" "numpy>=" \
pkgs/development/python-modules/pmdarima/default.nix-      --replace-fail "scipy==" "scipy>=" \
pkgs/development/python-modules/pmdarima/default.nix-      --replace-fail "statsmodels==" "statsmodels>="
pkgs/development/python-modules/pmdarima/default.nix-  '';
pkgs/development/python-modules/pmdarima/default.nix-
pkgs/development/python-modules/pmdarima/default.nix-  env = {
pkgs/development/python-modules/pmdarima/default.nix-    GITHUB_REF = "refs/tags/v${version}";
pkgs/development/python-modules/pmdarima/default.nix-  };
pkgs/development/python-modules/pmdarima/default.nix-
pkgs/development/python-modules/pmdarima/default.nix-  preBuild = ''
--
pkgs/development/python-modules/chai/default.nix-  version = "1.1.2";
pkgs/development/python-modules/chai/default.nix-  format = "setuptools";
--
pkgs/development/python-modules/array-api-strict/default.nix-
pkgs/development/python-modules/array-api-strict/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/array-api-strict/default.nix-    owner = "data-apis";
pkgs/development/python-modules/array-api-strict/default.nix-    repo = "array-api-strict";
pkgs/development/python-modules/array-api-strict/default.nix-    tag = version;
pkgs/development/python-modules/array-api-strict/default.nix-    hash = "sha256-m0uWaeUwHsWyAOxS7nxY8c+HWUhz+mOKNE4M0DsiClI=";
pkgs/development/python-modules/array-api-strict/default.nix-  };
pkgs/development/python-modules/array-api-strict/default.nix-
pkgs/development/python-modules/array-api-strict/default.nix-  postPatch = ''
pkgs/development/python-modules/array-api-strict/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/array-api-strict/default.nix-      --replace-fail "setuptools >= 61.0,<=75" "setuptools"
pkgs/development/python-modules/array-api-strict/default.nix-  '';
pkgs/development/python-modules/array-api-strict/default.nix-
pkgs/development/python-modules/array-api-strict/default.nix-  build-system = [
pkgs/development/python-modules/array-api-strict/default.nix-    setuptools
pkgs/development/python-modules/array-api-strict/default.nix-    setuptools-scm
pkgs/development/python-modules/array-api-strict/default.nix-  ];
pkgs/development/python-modules/array-api-strict/default.nix-
pkgs/development/python-modules/array-api-strict/default.nix-  dependencies = [ numpy ];
pkgs/development/python-modules/array-api-strict/default.nix-
--
--
pkgs/development/python-modules/djangorestframework-stubs/default.nix-
pkgs/development/python-modules/djangorestframework-stubs/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/djangorestframework-stubs/default.nix-    owner = "typeddjango";
pkgs/development/python-modules/djangorestframework-stubs/default.nix-    repo = "djangorestframework-stubs";
pkgs/development/python-modules/djangorestframework-stubs/default.nix-    tag = version;
pkgs/development/python-modules/djangorestframework-stubs/default.nix-    hash = "sha256-A6IyRJwuc0eqRtkCHtWN5C5yCMdgxfygqmpHV+/MJhE=";
pkgs/development/python-modules/djangorestframework-stubs/default.nix-  };
pkgs/development/python-modules/djangorestframework-stubs/default.nix-
pkgs/development/python-modules/djangorestframework-stubs/default.nix-  postPatch = ''
pkgs/development/python-modules/djangorestframework-stubs/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/djangorestframework-stubs/default.nix-      --replace-fail "<79.0.0" ""
pkgs/development/python-modules/djangorestframework-stubs/default.nix-  '';
pkgs/development/python-modules/djangorestframework-stubs/default.nix-
pkgs/development/python-modules/djangorestframework-stubs/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/djangorestframework-stubs/default.nix-
pkgs/development/python-modules/djangorestframework-stubs/default.nix-  dependencies = [
pkgs/development/python-modules/djangorestframework-stubs/default.nix-    django-stubs
pkgs/development/python-modules/djangorestframework-stubs/default.nix-    requests
pkgs/development/python-modules/djangorestframework-stubs/default.nix-    types-pyyaml
pkgs/development/python-modules/djangorestframework-stubs/default.nix-    types-requests
--
--
pkgs/development/python-modules/qiskit-finance/default.nix-  disabled = pythonOlder "3.6";
pkgs/development/python-modules/qiskit-finance/default.nix-
pkgs/development/python-modules/qiskit-finance/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/qiskit-finance/default.nix-    owner = "qiskit";
pkgs/development/python-modules/qiskit-finance/default.nix-    repo = pname;
pkgs/development/python-modules/qiskit-finance/default.nix-    rev = "refs/tags/${version}";
pkgs/development/python-modules/qiskit-finance/default.nix-    hash = "sha256-zYhYhojCzlENzgYSenwewjeVHUBX2X6eQbbzc9znBsk=";
pkgs/development/python-modules/qiskit-finance/default.nix-  };
pkgs/development/python-modules/qiskit-finance/default.nix-
pkgs/development/python-modules/qiskit-finance/default.nix-  postPatch = ''
pkgs/development/python-modules/qiskit-finance/default.nix:    substituteInPlace requirements.txt --replace "pandas<1.4.0" "pandas"
pkgs/development/python-modules/qiskit-finance/default.nix-  '';
pkgs/development/python-modules/qiskit-finance/default.nix-
pkgs/development/python-modules/qiskit-finance/default.nix-  nativeBuildInputs = [ setuptools ];
pkgs/development/python-modules/qiskit-finance/default.nix-
pkgs/development/python-modules/qiskit-finance/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/qiskit-finance/default.nix-    fastdtw
pkgs/development/python-modules/qiskit-finance/default.nix-    numpy
pkgs/development/python-modules/qiskit-finance/default.nix-    pandas
pkgs/development/python-modules/qiskit-finance/default.nix-    psutil
pkgs/development/python-modules/qiskit-finance/default.nix-    qiskit-terra
--
pkgs/development/python-modules/zope-security/default.nix-
pkgs/development/python-modules/zope-security/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/zope-security/default.nix-    owner = "zopefoundation";
pkgs/development/python-modules/zope-security/default.nix-    repo = "zope.security";
pkgs/development/python-modules/zope-security/default.nix-    tag = version;
pkgs/development/python-modules/zope-security/default.nix-    hash = "sha256-p+9pCcBsCJY/V6vraVZHMr5VwYHFe217AbRVoSnDphs=";
pkgs/development/python-modules/zope-security/default.nix-  };
pkgs/development/python-modules/zope-security/default.nix-
pkgs/development/python-modules/zope-security/default.nix-  postPatch = ''
pkgs/development/python-modules/zope-security/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/zope-security/default.nix-      --replace-fail "setuptools<74" "setuptools"
pkgs/development/python-modules/zope-security/default.nix-  '';
pkgs/development/python-modules/zope-security/default.nix-
pkgs/development/python-modules/zope-security/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/zope-security/default.nix-
pkgs/development/python-modules/zope-security/default.nix-  dependencies = [
pkgs/development/python-modules/zope-security/default.nix-    zope-component
pkgs/development/python-modules/zope-security/default.nix-    zope-i18nmessageid
pkgs/development/python-modules/zope-security/default.nix-    zope-interface
pkgs/development/python-modules/zope-security/default.nix-    zope-location
--
--
pkgs/development/python-modules/imgcat/default.nix-
pkgs/development/python-modules/imgcat/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/imgcat/default.nix-    owner = "wookayin";
pkgs/development/python-modules/imgcat/default.nix-    repo = "python-imgcat";
pkgs/development/python-modules/imgcat/default.nix-    tag = "v${version}";
pkgs/development/python-modules/imgcat/default.nix-    hash = "sha256-FsLa8Z4aKuj3E5twC2LTXZDM0apmyYfgeyZQu/wLdAo=";
pkgs/development/python-modules/imgcat/default.nix-  };
pkgs/development/python-modules/imgcat/default.nix-
pkgs/development/python-modules/imgcat/default.nix-  postPatch = ''
pkgs/development/python-modules/imgcat/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/imgcat/default.nix-      --replace-fail "'pytest-runner<5.0'" ""
pkgs/development/python-modules/imgcat/default.nix-  '';
pkgs/development/python-modules/imgcat/default.nix-
pkgs/development/python-modules/imgcat/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/imgcat/default.nix-
pkgs/development/python-modules/imgcat/default.nix-  nativeCheckInputs = [
pkgs/development/python-modules/imgcat/default.nix-    matplotlib
pkgs/development/python-modules/imgcat/default.nix-    numpy
pkgs/development/python-modules/imgcat/default.nix-    pillow
pkgs/development/python-modules/imgcat/default.nix-    pytestCheckHook
--
--
pkgs/development/python-modules/basedmypy/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/basedmypy/default.nix-    owner = "KotlinIsland";
pkgs/development/python-modules/basedmypy/default.nix-    repo = "basedmypy";
pkgs/development/python-modules/basedmypy/default.nix-    tag = "v${version}";
pkgs/development/python-modules/basedmypy/default.nix-    hash = "sha256-IzRKOReSgio5S5PG8iD9VQF9R1GEqBAIDeeCtq+ZVXg=";
pkgs/development/python-modules/basedmypy/default.nix-  };
pkgs/development/python-modules/basedmypy/default.nix-
pkgs/development/python-modules/basedmypy/default.nix-  postPatch = ''
pkgs/development/python-modules/basedmypy/default.nix:    substituteInPlace \
pkgs/development/python-modules/basedmypy/default.nix-      pyproject.toml \
pkgs/development/python-modules/basedmypy/default.nix-      --replace-warn 'types-setuptools==' 'types-setuptools>='
pkgs/development/python-modules/basedmypy/default.nix-  ''
pkgs/development/python-modules/basedmypy/default.nix-  # __closed__ returns None at runtime (not a bool)
pkgs/development/python-modules/basedmypy/default.nix-  + ''
pkgs/development/python-modules/basedmypy/default.nix:    substituteInPlace test-data/unit/lib-stub/typing_extensions.pyi \
pkgs/development/python-modules/basedmypy/default.nix-      --replace-fail "__closed__: bool" "__closed__: None"
pkgs/development/python-modules/basedmypy/default.nix-  '';
pkgs/development/python-modules/basedmypy/default.nix-
pkgs/development/python-modules/basedmypy/default.nix-  build-system = [
pkgs/development/python-modules/basedmypy/default.nix-    basedtyping
pkgs/development/python-modules/basedmypy/default.nix-    mypy-extensions
--
pkgs/development/python-modules/zope-lifecycleevent/default.nix-
pkgs/development/python-modules/zope-lifecycleevent/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/zope-lifecycleevent/default.nix-    owner = "zopefoundation";
pkgs/development/python-modules/zope-lifecycleevent/default.nix-    repo = "zope.lifecycleevent";
pkgs/development/python-modules/zope-lifecycleevent/default.nix-    tag = version;
pkgs/development/python-modules/zope-lifecycleevent/default.nix-    hash = "sha256-vTonbZSeQxnLA6y1wAnBpobEKAs+gaAYN25dx5Fla9k=";
pkgs/development/python-modules/zope-lifecycleevent/default.nix-  };
pkgs/development/python-modules/zope-lifecycleevent/default.nix-
pkgs/development/python-modules/zope-lifecycleevent/default.nix-  postPatch = ''
pkgs/development/python-modules/zope-lifecycleevent/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/zope-lifecycleevent/default.nix-      --replace-fail "setuptools <= 75.6.0" setuptools
pkgs/development/python-modules/zope-lifecycleevent/default.nix-  '';
pkgs/development/python-modules/zope-lifecycleevent/default.nix-
pkgs/development/python-modules/zope-lifecycleevent/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/zope-lifecycleevent/default.nix-
pkgs/development/python-modules/zope-lifecycleevent/default.nix-  dependencies = [
pkgs/development/python-modules/zope-lifecycleevent/default.nix-    zope-event
pkgs/development/python-modules/zope-lifecycleevent/default.nix-    zope-interface
pkgs/development/python-modules/zope-lifecycleevent/default.nix-  ];
pkgs/development/python-modules/zope-lifecycleevent/default.nix-
--
--
pkgs/development/python-modules/spacy/models.nix-      ++ lib.optionals (lang == "uk") [
pkgs/development/python-modules/spacy/models.nix-        pymorphy3
pkgs/development/python-modules/spacy/models.nix-        pymorphy3-dicts-uk
pkgs/development/python-modules/spacy/models.nix-      ]
pkgs/development/python-modules/spacy/models.nix-      ++ lib.optionals (lang == "zh") [ spacy-pkuseg ]
pkgs/development/python-modules/spacy/models.nix-      ++ lib.optionals requires-sentencepiece [ sentencepiece ];
pkgs/development/python-modules/spacy/models.nix-
pkgs/development/python-modules/spacy/models.nix-      postPatch =
pkgs/development/python-modules/spacy/models.nix-        lib.optionalString requires-protobuf ''
pkgs/development/python-modules/spacy/models.nix:          substituteInPlace meta.json \
pkgs/development/python-modules/spacy/models.nix-            --replace-fail "protobuf<3.21.0" "protobuf"
pkgs/development/python-modules/spacy/models.nix-        ''
pkgs/development/python-modules/spacy/models.nix-        + lib.optionalString (lang == "zh") ''
pkgs/development/python-modules/spacy/models.nix-          # Uses numpy 2.x, while the rest of the dependencies still uses
pkgs/development/python-modules/spacy/models.nix-          # numpy 1.x. Remove once all spaCy packages are updated for
pkgs/development/python-modules/spacy/models.nix-          # numpy 2.x.
pkgs/development/python-modules/spacy/models.nix:          substituteInPlace meta.json \
pkgs/development/python-modules/spacy/models.nix-            --replace-fail "spacy-pkuseg>=1.0.0,<2.0.0" "spacy-pkuseg"
pkgs/development/python-modules/spacy/models.nix-        '';
pkgs/development/python-modules/spacy/models.nix-
pkgs/development/python-modules/spacy/models.nix-      nativeBuildInputs = [ setuptools ] ++ lib.optionals requires-protobuf [ protobuf ];
pkgs/development/python-modules/spacy/models.nix-
pkgs/development/python-modules/spacy/models.nix-      pythonImportsCheck = [ pname ];
pkgs/development/python-modules/spacy/models.nix-
pkgs/development/python-modules/spacy/models.nix-      passthru.updateScript = writeScript "update-spacy-models" ''
pkgs/development/python-modules/spacy/models.nix-        #!${stdenv.shell}
pkgs/development/python-modules/spacy/models.nix-        set -eou pipefail
--
--
pkgs/development/python-modules/bleak-esphome/default.nix-
pkgs/development/python-modules/bleak-esphome/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/bleak-esphome/default.nix-    owner = "bluetooth-devices";
pkgs/development/python-modules/bleak-esphome/default.nix-    repo = "bleak-esphome";
pkgs/development/python-modules/bleak-esphome/default.nix-    tag = "v${version}";
pkgs/development/python-modules/bleak-esphome/default.nix-    hash = "sha256-L2/DtT1vEkP67oktLNix+/+eoVbJoMfUvW6232gSMCM=";
pkgs/development/python-modules/bleak-esphome/default.nix-  };
pkgs/development/python-modules/bleak-esphome/default.nix-
pkgs/development/python-modules/bleak-esphome/default.nix-  postPatch = ''
pkgs/development/python-modules/bleak-esphome/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/bleak-esphome/default.nix-      --replace-fail "setuptools>=75.8.2" setuptools
pkgs/development/python-modules/bleak-esphome/default.nix-  '';
pkgs/development/python-modules/bleak-esphome/default.nix-
pkgs/development/python-modules/bleak-esphome/default.nix-  build-system = [
pkgs/development/python-modules/bleak-esphome/default.nix-    cython
pkgs/development/python-modules/bleak-esphome/default.nix-    poetry-core
pkgs/development/python-modules/bleak-esphome/default.nix-    setuptools
pkgs/development/python-modules/bleak-esphome/default.nix-  ];
pkgs/development/python-modules/bleak-esphome/default.nix-
pkgs/development/python-modules/bleak-esphome/default.nix-  dependencies = [
--
--
pkgs/development/python-modules/osqp/default.nix-
pkgs/development/python-modules/osqp/default.nix-  disabled = pythonOlder "3.7";
pkgs/development/python-modules/osqp/default.nix-
pkgs/development/python-modules/osqp/default.nix-  src = fetchPypi {
pkgs/development/python-modules/osqp/default.nix-    inherit pname version;
pkgs/development/python-modules/osqp/default.nix-    hash = "sha256-sMXgpyHyHJckCXpP1QEIME0pZGjRJOFvNKxnBG9wIOE=";
pkgs/development/python-modules/osqp/default.nix-  };
pkgs/development/python-modules/osqp/default.nix-
pkgs/development/python-modules/osqp/default.nix-  postPatch = ''
pkgs/development/python-modules/osqp/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/osqp/default.nix-      --replace-fail "numpy >= 2.0.0" numpy
pkgs/development/python-modules/osqp/default.nix-  '';
pkgs/development/python-modules/osqp/default.nix-
pkgs/development/python-modules/osqp/default.nix-  dontUseCmakeConfigure = true;
pkgs/development/python-modules/osqp/default.nix-
pkgs/development/python-modules/osqp/default.nix-  nativeBuildInputs = [
pkgs/development/python-modules/osqp/default.nix-    cmake
pkgs/development/python-modules/osqp/default.nix-    numpy
pkgs/development/python-modules/osqp/default.nix-    oldest-supported-numpy
pkgs/development/python-modules/osqp/default.nix-    setuptools-scm
--
--
pkgs/development/python-modules/pynput/default.nix-    repo = "pynput";
pkgs/development/python-modules/pynput/default.nix-    tag = "v${version}";
pkgs/development/python-modules/pynput/default.nix-    hash = "sha256-rOkUyreS3JqEyubQUdNLJf5lDuFassDKrQrUXKrKlgI=";
pkgs/development/python-modules/pynput/default.nix-  };
pkgs/development/python-modules/pynput/default.nix-  passthru.updateScript = gitUpdater {
pkgs/development/python-modules/pynput/default.nix-    rev-prefix = "v";
pkgs/development/python-modules/pynput/default.nix-  };
pkgs/development/python-modules/pynput/default.nix-
pkgs/development/python-modules/pynput/default.nix-  postPatch = ''
pkgs/development/python-modules/pynput/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/pynput/default.nix-      --replace-fail "'sphinx >=1.3.1'," "" \
pkgs/development/python-modules/pynput/default.nix-      --replace-fail "'twine >=4.0']" "]"
pkgs/development/python-modules/pynput/default.nix-  '';
pkgs/development/python-modules/pynput/default.nix-
pkgs/development/python-modules/pynput/default.nix-  nativeBuildInputs = [
pkgs/development/python-modules/pynput/default.nix-    setuptools
pkgs/development/python-modules/pynput/default.nix-    setuptools-lint
pkgs/development/python-modules/pynput/default.nix-    sphinx
pkgs/development/python-modules/pynput/default.nix-  ];
pkgs/development/python-modules/pynput/default.nix-
--
pkgs/development/python-modules/facedancer/default.nix-  disabled = pythonOlder "3.10";
pkgs/development/python-modules/facedancer/default.nix-
pkgs/development/python-modules/facedancer/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/facedancer/default.nix-    owner = "greatscottgadgets";
pkgs/development/python-modules/facedancer/default.nix-    repo = "facedancer";
pkgs/development/python-modules/facedancer/default.nix-    tag = version;
pkgs/development/python-modules/facedancer/default.nix-    hash = "sha256-Qe8DPUKwlukPftc7SOZIcY/do/14UdS61WH0g5dFeMI=";
pkgs/development/python-modules/facedancer/default.nix-  };
pkgs/development/python-modules/facedancer/default.nix-
pkgs/development/python-modules/facedancer/default.nix-  postPatch = ''
pkgs/development/python-modules/facedancer/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/facedancer/default.nix-      --replace-fail '"setuptools-git-versioning<2"' "" \
pkgs/development/python-modules/facedancer/default.nix-      --replace-fail 'dynamic = ["version"]' 'version = "${version}"'
pkgs/development/python-modules/facedancer/default.nix-  '';
pkgs/development/python-modules/facedancer/default.nix-
pkgs/development/python-modules/facedancer/default.nix-  build-system = [
pkgs/development/python-modules/facedancer/default.nix-    setuptools
pkgs/development/python-modules/facedancer/default.nix-  ];
pkgs/development/python-modules/facedancer/default.nix-
pkgs/development/python-modules/facedancer/default.nix-  dependencies = [
pkgs/development/python-modules/facedancer/default.nix-    pyusb
--
--
pkgs/development/python-modules/pulsectl-asyncio/default.nix-  disabled = pythonOlder "3.7";
pkgs/development/python-modules/pulsectl-asyncio/default.nix-
pkgs/development/python-modules/pulsectl-asyncio/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/pulsectl-asyncio/default.nix-    owner = "mhthies";
pkgs/development/python-modules/pulsectl-asyncio/default.nix-    repo = "pulsectl-asyncio";
pkgs/development/python-modules/pulsectl-asyncio/default.nix-    tag = "v${version}";
pkgs/development/python-modules/pulsectl-asyncio/default.nix-    hash = "sha256-lHVLrkFdNM8Y4t6TcXYnX8sQ4COrW3vV2sTDWeI4xZU=";
pkgs/development/python-modules/pulsectl-asyncio/default.nix-  };
pkgs/development/python-modules/pulsectl-asyncio/default.nix-
pkgs/development/python-modules/pulsectl-asyncio/default.nix-  postPatch = ''
pkgs/development/python-modules/pulsectl-asyncio/default.nix:    substituteInPlace setup.cfg --replace-fail "pulsectl >=23.5.0,<=24.11.0" "pulsectl >=23.5.0"
pkgs/development/python-modules/pulsectl-asyncio/default.nix-  '';
pkgs/development/python-modules/pulsectl-asyncio/default.nix-
pkgs/development/python-modules/pulsectl-asyncio/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/pulsectl-asyncio/default.nix-
pkgs/development/python-modules/pulsectl-asyncio/default.nix-  dependencies = [ pulsectl ];
pkgs/development/python-modules/pulsectl-asyncio/default.nix-
pkgs/development/python-modules/pulsectl-asyncio/default.nix-  # Tests require a running pulseaudio instance
pkgs/development/python-modules/pulsectl-asyncio/default.nix-  doCheck = false;
pkgs/development/python-modules/pulsectl-asyncio/default.nix-
pkgs/development/python-modules/pulsectl-asyncio/default.nix-  pythonImportsCheck = [ "pulsectl_asyncio" ];
--
pkgs/development/python-modules/awesome-slugify/default.nix-  version = "1.6.5";
pkgs/development/python-modules/awesome-slugify/default.nix-  format = "setuptools";
pkgs/development/python-modules/awesome-slugify/default.nix-
pkgs/development/python-modules/awesome-slugify/default.nix-  src = fetchPypi {
pkgs/development/python-modules/awesome-slugify/default.nix-    inherit pname version;
pkgs/development/python-modules/awesome-slugify/default.nix-    sha256 = "0wgxrhr8s5vk2xmcz9s1z1aml4ppawmhkbggl9rp94c747xc7pmv";
pkgs/development/python-modules/awesome-slugify/default.nix-  };
pkgs/development/python-modules/awesome-slugify/default.nix-
pkgs/development/python-modules/awesome-slugify/default.nix-  prePatch = ''
pkgs/development/python-modules/awesome-slugify/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/awesome-slugify/default.nix-        --replace 'Unidecode>=0.04.14,<0.05' 'Unidecode>=0.04.14'
pkgs/development/python-modules/awesome-slugify/default.nix-  '';
pkgs/development/python-modules/awesome-slugify/default.nix-
pkgs/development/python-modules/awesome-slugify/default.nix-  patches = [
pkgs/development/python-modules/awesome-slugify/default.nix-    ./slugify_filename_test.patch # fixes broken test by new unidecode
pkgs/development/python-modules/awesome-slugify/default.nix-  ];
pkgs/development/python-modules/awesome-slugify/default.nix-
pkgs/development/python-modules/awesome-slugify/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/awesome-slugify/default.nix-    unidecode
pkgs/development/python-modules/awesome-slugify/default.nix-    regex
--
--
pkgs/development/python-modules/betterproto/default.nix-
pkgs/development/python-modules/betterproto/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/betterproto/default.nix-    owner = "danielgtaylor";
pkgs/development/python-modules/betterproto/default.nix-    repo = "python-betterproto";
pkgs/development/python-modules/betterproto/default.nix-    tag = "v.${version}";
pkgs/development/python-modules/betterproto/default.nix-    hash = "sha256-ZuVq4WERXsRFUPNNTNp/eisWX1MyI7UtwqEI8X93wYI=";
pkgs/development/python-modules/betterproto/default.nix-  };
pkgs/development/python-modules/betterproto/default.nix-
pkgs/development/python-modules/betterproto/default.nix-  postPatch = ''
pkgs/development/python-modules/betterproto/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/betterproto/default.nix-      --replace-fail "poetry-core>=1.0.0,<2" "poetry-core"
pkgs/development/python-modules/betterproto/default.nix-  '';
pkgs/development/python-modules/betterproto/default.nix-
pkgs/development/python-modules/betterproto/default.nix-  build-system = [ poetry-core ];
pkgs/development/python-modules/betterproto/default.nix-
pkgs/development/python-modules/betterproto/default.nix-  dependencies = [
pkgs/development/python-modules/betterproto/default.nix-    grpclib
pkgs/development/python-modules/betterproto/default.nix-    python-dateutil
pkgs/development/python-modules/betterproto/default.nix-    typing-extensions
pkgs/development/python-modules/betterproto/default.nix-  ];
--
--
pkgs/development/python-modules/makefun/default.nix-  version = "1.16.0";
pkgs/development/python-modules/makefun/default.nix-  pyproject = true;
pkgs/development/python-modules/makefun/default.nix-
pkgs/development/python-modules/makefun/default.nix-  src = fetchPypi {
pkgs/development/python-modules/makefun/default.nix-    inherit pname version;
pkgs/development/python-modules/makefun/default.nix-    hash = "sha256-4UYBgxVwv/H21+aIKLzTDS9YVvJLrV3gzLIpIc7ryUc=";
pkgs/development/python-modules/makefun/default.nix-  };
pkgs/development/python-modules/makefun/default.nix-
pkgs/development/python-modules/makefun/default.nix-  postPatch = ''
pkgs/development/python-modules/makefun/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/makefun/default.nix-      --replace-fail '"setuptools>=39.2,<72"' '"setuptools"'
pkgs/development/python-modules/makefun/default.nix-  '';
pkgs/development/python-modules/makefun/default.nix-
pkgs/development/python-modules/makefun/default.nix-  build-system = [
pkgs/development/python-modules/makefun/default.nix-    setuptools
pkgs/development/python-modules/makefun/default.nix-    setuptools-scm
pkgs/development/python-modules/makefun/default.nix-  ];
pkgs/development/python-modules/makefun/default.nix-
pkgs/development/python-modules/makefun/default.nix-  nativeCheckInputs = [ pytest7CheckHook ];
pkgs/development/python-modules/makefun/default.nix-
--
--
pkgs/development/python-modules/apollo-fpga/default.nix-
pkgs/development/python-modules/apollo-fpga/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/apollo-fpga/default.nix-    owner = "greatscottgadgets";
pkgs/development/python-modules/apollo-fpga/default.nix-    repo = "apollo";
pkgs/development/python-modules/apollo-fpga/default.nix-    tag = "v${version}";
pkgs/development/python-modules/apollo-fpga/default.nix-    hash = "sha256-EDI+bRDePEbkxfQKuDgRsJtlAE0jqcIoQHjpgW0jIoY=";
pkgs/development/python-modules/apollo-fpga/default.nix-  };
pkgs/development/python-modules/apollo-fpga/default.nix-
pkgs/development/python-modules/apollo-fpga/default.nix-  postPatch = ''
pkgs/development/python-modules/apollo-fpga/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/apollo-fpga/default.nix-      --replace-fail '"setuptools-git-versioning<2"' "" \
pkgs/development/python-modules/apollo-fpga/default.nix-      --replace-fail 'dynamic = ["version"]' 'version = "${version}"'
pkgs/development/python-modules/apollo-fpga/default.nix-  '';
pkgs/development/python-modules/apollo-fpga/default.nix-
pkgs/development/python-modules/apollo-fpga/default.nix-  build-system = [
pkgs/development/python-modules/apollo-fpga/default.nix-    setuptools
pkgs/development/python-modules/apollo-fpga/default.nix-  ];
pkgs/development/python-modules/apollo-fpga/default.nix-
pkgs/development/python-modules/apollo-fpga/default.nix-  dependencies = [
pkgs/development/python-modules/apollo-fpga/default.nix-    deprecation
--
--
pkgs/development/python-modules/pyexcel-xls/default.nix-    xlwt
pkgs/development/python-modules/pyexcel-xls/default.nix-  ];
pkgs/development/python-modules/pyexcel-xls/default.nix-
pkgs/development/python-modules/pyexcel-xls/default.nix-  nativeCheckInputs = [
pkgs/development/python-modules/pyexcel-xls/default.nix-    pytestCheckHook
pkgs/development/python-modules/pyexcel-xls/default.nix-    pyexcel
pkgs/development/python-modules/pyexcel-xls/default.nix-    pytest-cov-stub
pkgs/development/python-modules/pyexcel-xls/default.nix-  ];
pkgs/development/python-modules/pyexcel-xls/default.nix-
pkgs/development/python-modules/pyexcel-xls/default.nix-  postPatch = ''
pkgs/development/python-modules/pyexcel-xls/default.nix:    substituteInPlace setup.py --replace "xlrd<2" "xlrd<3"
pkgs/development/python-modules/pyexcel-xls/default.nix-  '';
pkgs/development/python-modules/pyexcel-xls/default.nix-
pkgs/development/python-modules/pyexcel-xls/default.nix-  meta = {
pkgs/development/python-modules/pyexcel-xls/default.nix-    description = "Wrapper library to read, manipulate and write data in xls using xlrd and xlwt";
pkgs/development/python-modules/pyexcel-xls/default.nix-    homepage = "http://docs.pyexcel.org/";
pkgs/development/python-modules/pyexcel-xls/default.nix-    license = lib.licenses.bsd3;
pkgs/development/python-modules/pyexcel-xls/default.nix-    maintainers = [ ];
pkgs/development/python-modules/pyexcel-xls/default.nix-  };
pkgs/development/python-modules/pyexcel-xls/default.nix-}
--
--
pkgs/development/python-modules/numpy/1.nix-    #   TypeError: dist must be a Distribution instance
pkgs/development/python-modules/numpy/1.nix-    rm numpy/core/tests/test_cython.py
pkgs/development/python-modules/numpy/1.nix-
pkgs/development/python-modules/numpy/1.nix-    patchShebangs numpy/_build_utils/*.py
pkgs/development/python-modules/numpy/1.nix-
pkgs/development/python-modules/numpy/1.nix-    # remove needless reference to full Python path stored in built wheel
pkgs/development/python-modules/numpy/1.nix:    substituteInPlace numpy/meson.build \
pkgs/development/python-modules/numpy/1.nix-      --replace 'py.full_path()' "'python'"
pkgs/development/python-modules/numpy/1.nix-
pkgs/development/python-modules/numpy/1.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/numpy/1.nix-      --replace-fail "Cython>=0.29.34,<3.1" Cython \
pkgs/development/python-modules/numpy/1.nix-      --replace-fail "meson-python>=0.15.0,<0.16.0" "meson-python"
pkgs/development/python-modules/numpy/1.nix-  '';
pkgs/development/python-modules/numpy/1.nix-
pkgs/development/python-modules/numpy/1.nix-  nativeBuildInputs = [
pkgs/development/python-modules/numpy/1.nix-    cython
pkgs/development/python-modules/numpy/1.nix-    gfortran
pkgs/development/python-modules/numpy/1.nix-    meson-python
pkgs/development/python-modules/numpy/1.nix-    pkg-config
pkgs/development/python-modules/numpy/1.nix-  ]
--
pkgs/development/python-modules/rchitect/default.nix-  disabled = pythonOlder "3.9";
--
pkgs/development/python-modules/torch/source/default.nix-  + lib.optionalString rocmSupport ''
pkgs/development/python-modules/torch/source/default.nix:    substituteInPlace $dev/share/cmake/Tensorpipe/TensorpipeTargets-release.cmake \
pkgs/development/python-modules/torch/source/default.nix-      --replace-fail "\''${_IMPORT_PREFIX}/lib64" "$lib/lib"
pkgs/development/python-modules/torch/source/default.nix-
pkgs/development/python-modules/torch/source/default.nix:    substituteInPlace $dev/share/cmake/ATen/ATenConfig.cmake \
pkgs/development/python-modules/torch/source/default.nix-      --replace-fail "/build/${src.name}/torch/include" "$dev/include"
pkgs/development/python-modules/torch/source/default.nix-  '';
pkgs/development/python-modules/torch/source/default.nix-
pkgs/development/python-modules/torch/source/default.nix-  postFixup = ''
pkgs/development/python-modules/torch/source/default.nix-    mkdir -p "$cxxdev/nix-support"
pkgs/development/python-modules/torch/source/default.nix-    printWords "''${propagatedCxxBuildInputs[@]}" >> "$cxxdev/nix-support/propagated-build-inputs"
pkgs/development/python-modules/torch/source/default.nix-  ''
pkgs/development/python-modules/torch/source/default.nix-  + lib.optionalString stdenv.hostPlatform.isDarwin ''
pkgs/development/python-modules/torch/source/default.nix-    for f in $(ls $lib/lib/*.dylib); do
pkgs/development/python-modules/torch/source/default.nix-        install_name_tool -id $lib/lib/$(basename $f) $f || true
--
pkgs/development/python-modules/axis/default.nix-  disabled = pythonOlder "3.12";
pkgs/development/python-modules/axis/default.nix-
pkgs/development/python-modules/axis/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/axis/default.nix-    owner = "Kane610";
pkgs/development/python-modules/axis/default.nix-    repo = "axis";
--
pkgs/development/python-modules/zconfig/default.nix-  pyproject = true;
pkgs/development/python-modules/zconfig/default.nix-
pkgs/development/python-modules/zconfig/default.nix-  src = fetchPypi {
pkgs/development/python-modules/zconfig/default.nix-    inherit pname version;
pkgs/development/python-modules/zconfig/default.nix-    hash = "sha256-oOS1J3xM7oBgzjNaV4rEWPgsJArpaxZlkgDbxNmL/M4=";
pkgs/development/python-modules/zconfig/default.nix-  };
pkgs/development/python-modules/zconfig/default.nix-
pkgs/development/python-modules/zconfig/default.nix-  patches = lib.optional stdenv.hostPlatform.isMusl ./remove-setlocale-test.patch;
pkgs/development/python-modules/zconfig/default.nix-
pkgs/development/python-modules/zconfig/default.nix-  postPatch = ''
pkgs/development/python-modules/zconfig/default.nix:    substituteInPlace pyproject.toml --replace-fail 'setuptools <= 75.6.0' 'setuptools'
pkgs/development/python-modules/zconfig/default.nix-  '';
pkgs/development/python-modules/zconfig/default.nix-
pkgs/development/python-modules/zconfig/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/zconfig/default.nix-
pkgs/development/python-modules/zconfig/default.nix-  buildInputs = [
pkgs/development/python-modules/zconfig/default.nix-    docutils
pkgs/development/python-modules/zconfig/default.nix-    manuel
pkgs/development/python-modules/zconfig/default.nix-  ];
pkgs/development/python-modules/zconfig/default.nix-
pkgs/development/python-modules/zconfig/default.nix-  dependencies = [ zope-testrunner ];
--
pkgs/development/python-modules/whisperx/default.nix-
pkgs/development/python-modules/whisperx/default.nix-  # As `makeWrapperArgs` does not apply to the module, and whisperx depends on `ffmpeg`,
pkgs/development/python-modules/whisperx/default.nix-  # we replace the `"ffmpeg"` string in `subprocess.run` with the full path to the binary.
pkgs/development/python-modules/whisperx/default.nix-  # This works for both the program and the module.
pkgs/development/python-modules/whisperx/default.nix-  # Every update, the codebase should be checked for further instances of `ffmpeg` calls.
pkgs/development/python-modules/whisperx/default.nix-  postPatch = ''
pkgs/development/python-modules/whisperx/default.nix:    substituteInPlace whisperx/audio.py --replace-fail \
pkgs/development/python-modules/whisperx/default.nix-      '"ffmpeg"' '"${lib.getExe ffmpeg}"'
pkgs/development/python-modules/whisperx/default.nix-  '';
pkgs/development/python-modules/whisperx/default.nix-
pkgs/development/python-modules/whisperx/default.nix-  # > Checking runtime dependencies for whisperx-3.3.2-py3-none-any.whl
pkgs/development/python-modules/whisperx/default.nix-  # >   - faster-whisper==1.1.0 not satisfied by version 1.1.1
pkgs/development/python-modules/whisperx/default.nix-  # This has been updated on main, so we expect this clause to be removed upon the next update.
pkgs/development/python-modules/whisperx/default.nix-  pythonRelaxDeps = [ "faster-whisper" ];
pkgs/development/python-modules/whisperx/default.nix-
pkgs/development/python-modules/whisperx/default.nix-  # Import check fails due on `aarch64-linux` ONLY in the sandbox due to onnxruntime
pkgs/development/python-modules/whisperx/default.nix-  # not finding its default logger, which then promptly segfaults.
--
pkgs/development/python-modules/distributed/default.nix-  pyproject = true;
pkgs/development/python-modules/distributed/default.nix-
pkgs/development/python-modules/distributed/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/distributed/default.nix-    owner = "dask";
pkgs/development/python-modules/distributed/default.nix-    repo = "distributed";
pkgs/development/python-modules/distributed/default.nix-    tag = version;
pkgs/development/python-modules/distributed/default.nix-    hash = "sha256-np4hCamNTbnmLdfjFeHsxEEm9XI1O0kOczDe1YjSziw=";
pkgs/development/python-modules/distributed/default.nix-  };
pkgs/development/python-modules/distributed/default.nix-
pkgs/development/python-modules/distributed/default.nix-  postPatch = ''
pkgs/development/python-modules/distributed/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/distributed/default.nix-      --replace-fail "versioneer[toml]==" "versioneer[toml]>=" \
pkgs/development/python-modules/distributed/default.nix-      --replace-fail 'dynamic = ["version"]' 'version = "${version}"'
pkgs/development/python-modules/distributed/default.nix-  '';
pkgs/development/python-modules/distributed/default.nix-
pkgs/development/python-modules/distributed/default.nix-  build-system = [
pkgs/development/python-modules/distributed/default.nix-    setuptools
pkgs/development/python-modules/distributed/default.nix-    setuptools-scm
pkgs/development/python-modules/distributed/default.nix-    versioneer
pkgs/development/python-modules/distributed/default.nix-  ]
pkgs/development/python-modules/distributed/default.nix-  ++ versioneer.optional-dependencies.toml;
--
--
pkgs/development/python-modules/rpcq/default.nix-
pkgs/development/python-modules/rpcq/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/rpcq/default.nix-    owner = "rigetti";
pkgs/development/python-modules/rpcq/default.nix-    repo = "rpcq";
pkgs/development/python-modules/rpcq/default.nix-    tag = "v${version}";
pkgs/development/python-modules/rpcq/default.nix-    hash = "sha256-J7jtGXJIF3jp0a0IQZmSR4TWf9D02Luau+Bupmi/d68=";
pkgs/development/python-modules/rpcq/default.nix-  };
pkgs/development/python-modules/rpcq/default.nix-
pkgs/development/python-modules/rpcq/default.nix-  postPatch = ''
pkgs/development/python-modules/rpcq/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/rpcq/default.nix-      --replace "msgpack>=0.6,<1.0" "msgpack"
pkgs/development/python-modules/rpcq/default.nix-  '';
pkgs/development/python-modules/rpcq/default.nix-
pkgs/development/python-modules/rpcq/default.nix-  nativeBuildInputs = [ setuptools ];
pkgs/development/python-modules/rpcq/default.nix-
pkgs/development/python-modules/rpcq/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/rpcq/default.nix-    msgpack
pkgs/development/python-modules/rpcq/default.nix-    python-rapidjson
pkgs/development/python-modules/rpcq/default.nix-    pyzmq
pkgs/development/python-modules/rpcq/default.nix-    ruamel-yaml
--
--
pkgs/development/python-modules/libsoundtouch/default.nix-
pkgs/development/python-modules/libsoundtouch/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/libsoundtouch/default.nix-    owner = "CharlesBlonde";
pkgs/development/python-modules/libsoundtouch/default.nix-    repo = "libsoundtouch";
pkgs/development/python-modules/libsoundtouch/default.nix-    tag = version;
pkgs/development/python-modules/libsoundtouch/default.nix-    hash = "sha256-am8nHPdtKMh8ZA/jKgz2jnltpvgEga8/BjvP5nrhgvI=";
pkgs/development/python-modules/libsoundtouch/default.nix-  };
pkgs/development/python-modules/libsoundtouch/default.nix-
pkgs/development/python-modules/libsoundtouch/default.nix-  postPatch = ''
pkgs/development/python-modules/libsoundtouch/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/libsoundtouch/default.nix-      --replace-fail "'enum-compat>=0.0.2'," ""
pkgs/development/python-modules/libsoundtouch/default.nix-  '';
pkgs/development/python-modules/libsoundtouch/default.nix-
pkgs/development/python-modules/libsoundtouch/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/libsoundtouch/default.nix-
pkgs/development/python-modules/libsoundtouch/default.nix-  dependencies = [
pkgs/development/python-modules/libsoundtouch/default.nix-    requests
pkgs/development/python-modules/libsoundtouch/default.nix-    websocket-client
pkgs/development/python-modules/libsoundtouch/default.nix-    zeroconf
pkgs/development/python-modules/libsoundtouch/default.nix-  ];
--
--
pkgs/development/python-modules/pyviz-comms/default.nix-  pyproject = true;
pkgs/development/python-modules/pyviz-comms/default.nix-
pkgs/development/python-modules/pyviz-comms/default.nix-  src = fetchPypi {
pkgs/development/python-modules/pyviz-comms/default.nix-    pname = "pyviz_comms";
pkgs/development/python-modules/pyviz-comms/default.nix-    inherit version;
pkgs/development/python-modules/pyviz-comms/default.nix-    hash = "sha256-c9ZrYgOQ2XlZssTYosB3jUH+IFgb5HF/AeRrj66MVpU=";
pkgs/development/python-modules/pyviz-comms/default.nix-  };
pkgs/development/python-modules/pyviz-comms/default.nix-
pkgs/development/python-modules/pyviz-comms/default.nix-  postPatch = ''
pkgs/development/python-modules/pyviz-comms/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/pyviz-comms/default.nix-      --replace-fail '"jupyterlab>=4.0.0,<5",' ""
pkgs/development/python-modules/pyviz-comms/default.nix-  '';
pkgs/development/python-modules/pyviz-comms/default.nix-
pkgs/development/python-modules/pyviz-comms/default.nix-  build-system = [
pkgs/development/python-modules/pyviz-comms/default.nix-    hatch-jupyter-builder
pkgs/development/python-modules/pyviz-comms/default.nix-    hatch-nodejs-version
pkgs/development/python-modules/pyviz-comms/default.nix-    hatchling
pkgs/development/python-modules/pyviz-comms/default.nix-  ];
pkgs/development/python-modules/pyviz-comms/default.nix-
pkgs/development/python-modules/pyviz-comms/default.nix-  dependencies = [ param ];
--
--
pkgs/development/python-modules/wxpython/4.2.nix-    which
--
pkgs/development/python-modules/wagtail-modeladmin/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/wagtail-modeladmin/default.nix-    owner = "wagtail-nest";
pkgs/development/python-modules/wagtail-modeladmin/default.nix-    repo = "wagtail-modeladmin";
pkgs/development/python-modules/wagtail-modeladmin/default.nix-    tag = "v${version}";
pkgs/development/python-modules/wagtail-modeladmin/default.nix-    hash = "sha256-P75jrH4fMODZHht+RAOd0/MutxsWtmui5Kxk8F/Ew0Q=";
pkgs/development/python-modules/wagtail-modeladmin/default.nix-  };
pkgs/development/python-modules/wagtail-modeladmin/default.nix-
pkgs/development/python-modules/wagtail-modeladmin/default.nix-  # Fail with `AssertionError`
pkgs/development/python-modules/wagtail-modeladmin/default.nix-  # AssertionError: <Warning: level=30,... > not found in [<Warning: ...>]
pkgs/development/python-modules/wagtail-modeladmin/default.nix-  postPatch = ''
pkgs/development/python-modules/wagtail-modeladmin/default.nix:    substituteInPlace wagtail_modeladmin/test/tests/test_simple_modeladmin.py \
pkgs/development/python-modules/wagtail-modeladmin/default.nix-      --replace-fail \
pkgs/development/python-modules/wagtail-modeladmin/default.nix-        "def test_model_with_single_tabbed_panel_only(" \
pkgs/development/python-modules/wagtail-modeladmin/default.nix-        "def no_test_model_with_single_tabbed_panel_only(" \
pkgs/development/python-modules/wagtail-modeladmin/default.nix-      --replace-fail \
pkgs/development/python-modules/wagtail-modeladmin/default.nix-        "def test_model_with_two_tabbed_panels_only(" \
pkgs/development/python-modules/wagtail-modeladmin/default.nix-        "def no_test_model_with_two_tabbed_panels_only("
pkgs/development/python-modules/wagtail-modeladmin/default.nix-  '';
pkgs/development/python-modules/wagtail-modeladmin/default.nix-
--
pkgs/development/python-modules/zope-configuration/default.nix-
pkgs/development/python-modules/zope-configuration/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/zope-configuration/default.nix-    owner = "zopefoundation";
pkgs/development/python-modules/zope-configuration/default.nix-    repo = "zope.configuration";
pkgs/development/python-modules/zope-configuration/default.nix-    tag = version;
pkgs/development/python-modules/zope-configuration/default.nix-    hash = "sha256-dkEVIHaXk/oP4uYYzI1hgSnPZXBMDjDu97zmOXnj9NA=";
pkgs/development/python-modules/zope-configuration/default.nix-  };
pkgs/development/python-modules/zope-configuration/default.nix-
pkgs/development/python-modules/zope-configuration/default.nix-  postPatch = ''
pkgs/development/python-modules/zope-configuration/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/zope-configuration/default.nix-      --replace-fail "setuptools < 74" "setuptools"
pkgs/development/python-modules/zope-configuration/default.nix-  '';
pkgs/development/python-modules/zope-configuration/default.nix-
pkgs/development/python-modules/zope-configuration/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/zope-configuration/default.nix-
pkgs/development/python-modules/zope-configuration/default.nix-  dependencies = [
pkgs/development/python-modules/zope-configuration/default.nix-    zope-i18nmessageid
pkgs/development/python-modules/zope-configuration/default.nix-    zope-interface
pkgs/development/python-modules/zope-configuration/default.nix-    zope-schema
pkgs/development/python-modules/zope-configuration/default.nix-  ];
--
--
pkgs/development/python-modules/ipfshttpclient/default.nix-    # Use pytest-order instead of pytest-ordering since the latter is unmaintained and broken
pkgs/development/python-modules/ipfshttpclient/default.nix:    substituteInPlace test/run-tests.py \
pkgs/development/python-modules/ipfshttpclient/default.nix-      --replace 'pytest_ordering' 'pytest_order'
pkgs/development/python-modules/ipfshttpclient/default.nix:    substituteInPlace test/functional/test_miscellaneous.py \
pkgs/development/python-modules/ipfshttpclient/default.nix-      --replace '@pytest.mark.last' '@pytest.mark.order("last")'
pkgs/development/python-modules/ipfshttpclient/default.nix-
pkgs/development/python-modules/ipfshttpclient/default.nix-    # Until a proper fix is created, just skip these tests
pkgs/development/python-modules/ipfshttpclient/default.nix-    # and ignore any breakage that may result from the API change in IPFS
pkgs/development/python-modules/ipfshttpclient/default.nix-    # See https://github.com/ipfs-shipyard/py-ipfs-http-client/issues/308
pkgs/development/python-modules/ipfshttpclient/default.nix:    substituteInPlace test/functional/test_pubsub.py \
pkgs/development/python-modules/ipfshttpclient/default.nix-      --replace '# the message that will be published' 'pytest.skip("This test fails because of an incompatibility with the experimental PubSub feature in IPFS>=0.11.0")' \
pkgs/development/python-modules/ipfshttpclient/default.nix-      --replace '# subscribe to the topic testing'     'pytest.skip("This test fails because of an incompatibility with the experimental PubSub feature in IPFS>=0.11.0")'
pkgs/development/python-modules/ipfshttpclient/default.nix:    substituteInPlace test/functional/test_other.py \
pkgs/development/python-modules/ipfshttpclient/default.nix-      --replace 'import ipfshttpclient' 'import ipfshttpclient; import pytest' \
pkgs/development/python-modules/ipfshttpclient/default.nix-      --replace 'assert ipfs_is_available' 'pytest.skip("Unknown test failure with IPFS >=0.11.0"); assert ipfs_is_available'
pkgs/development/python-modules/ipfshttpclient/default.nix-  '';
pkgs/development/python-modules/ipfshttpclient/default.nix-
pkgs/development/python-modules/ipfshttpclient/default.nix-  checkPhase = ''
pkgs/development/python-modules/ipfshttpclient/default.nix-    runHook preCheck
pkgs/development/python-modules/ipfshttpclient/default.nix-
pkgs/development/python-modules/ipfshttpclient/default.nix-    ${python.interpreter} -X utf8 test/run-tests.py
pkgs/development/python-modules/ipfshttpclient/default.nix-
pkgs/development/python-modules/ipfshttpclient/default.nix-    runHook postCheck
--
pkgs/development/python-modules/awesomeversion/default.nix-
--
pkgs/development/python-modules/mlx/default.nix-    };
pkgs/development/python-modules/mlx/default.nix-
pkgs/development/python-modules/mlx/default.nix-    patches = [
pkgs/development/python-modules/mlx/default.nix-      (replaceVars ./darwin-build-fixes.patch {
pkgs/development/python-modules/mlx/default.nix-        sdkVersion = apple-sdk_14.version;
pkgs/development/python-modules/mlx/default.nix-      })
pkgs/development/python-modules/mlx/default.nix-    ];
pkgs/development/python-modules/mlx/default.nix-
pkgs/development/python-modules/mlx/default.nix-    postPatch = ''
pkgs/development/python-modules/mlx/default.nix:      substituteInPlace pyproject.toml \
pkgs/development/python-modules/mlx/default.nix-        --replace-fail "nanobind==2.4.0" "nanobind>=2.4.0"
pkgs/development/python-modules/mlx/default.nix-
pkgs/development/python-modules/mlx/default.nix:      substituteInPlace mlx/backend/cpu/jit_compiler.cpp \
pkgs/development/python-modules/mlx/default.nix-        --replace-fail "g++" "$CXX"
pkgs/development/python-modules/mlx/default.nix-    '';
pkgs/development/python-modules/mlx/default.nix-
pkgs/development/python-modules/mlx/default.nix-    dontUseCmakeConfigure = true;
pkgs/development/python-modules/mlx/default.nix-
pkgs/development/python-modules/mlx/default.nix-    enableParallelBuilding = true;
pkgs/development/python-modules/mlx/default.nix-
pkgs/development/python-modules/mlx/default.nix-    # Allows multiple cores to be used in Python builds.
--
pkgs/development/python-modules/ssdeep/default.nix-    changelog = "https://github.com/DinoTools/python-ssdeep/blob/${version}/CHANGELOG.rst";
pkgs/development/python-modules/ssdeep/default.nix-    license = licenses.lgpl3Plus;
--
pkgs/development/python-modules/myfitnesspal/default.nix-  nativeCheckInputs = [
pkgs/development/python-modules/myfitnesspal/default.nix-    mock
pkgs/development/python-modules/myfitnesspal/default.nix-    pytestCheckHook
pkgs/development/python-modules/myfitnesspal/default.nix-  ];
pkgs/development/python-modules/myfitnesspal/default.nix-
pkgs/development/python-modules/myfitnesspal/default.nix-  postPatch = ''
pkgs/development/python-modules/myfitnesspal/default.nix-    # Remove overly restrictive version constraints
pkgs/development/python-modules/myfitnesspal/default.nix-    sed -i -e "s/>=.*//" requirements.txt
pkgs/development/python-modules/myfitnesspal/default.nix-
pkgs/development/python-modules/myfitnesspal/default.nix-    # https://github.com/coddingtonbear/python-measurement/pull/8
pkgs/development/python-modules/myfitnesspal/default.nix:    substituteInPlace tests/test_client.py \
pkgs/development/python-modules/myfitnesspal/default.nix-      --replace-fail "Weight" "Mass" \
pkgs/development/python-modules/myfitnesspal/default.nix-      --replace-fail '"Mass"' '"Weight"'
pkgs/development/python-modules/myfitnesspal/default.nix-  '';
pkgs/development/python-modules/myfitnesspal/default.nix-
pkgs/development/python-modules/myfitnesspal/default.nix-  disabledTests = [
pkgs/development/python-modules/myfitnesspal/default.nix-    # Integration tests require an account to be set
pkgs/development/python-modules/myfitnesspal/default.nix-    "test_integration"
--
pkgs/development/python-modules/zope-proxy/default.nix-
pkgs/development/python-modules/zope-proxy/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/zope-proxy/default.nix-    owner = "zopefoundation";
pkgs/development/python-modules/zope-proxy/default.nix-    repo = "zope.proxy";
pkgs/development/python-modules/zope-proxy/default.nix-    tag = version;
pkgs/development/python-modules/zope-proxy/default.nix-    hash = "sha256-RgkUojCAfwAGv8Jek2Ucg0KMtPviwXjuiO70iisParM=";
pkgs/development/python-modules/zope-proxy/default.nix-  };
pkgs/development/python-modules/zope-proxy/default.nix-
pkgs/development/python-modules/zope-proxy/default.nix-  postPatch = ''
pkgs/development/python-modules/zope-proxy/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/zope-proxy/default.nix-      --replace-fail "setuptools<74" "setuptools"
pkgs/development/python-modules/zope-proxy/default.nix-  '';
pkgs/development/python-modules/zope-proxy/default.nix-
pkgs/development/python-modules/zope-proxy/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/zope-proxy/default.nix-
pkgs/development/python-modules/zope-proxy/default.nix-  dependencies = [ zope-interface ];
pkgs/development/python-modules/zope-proxy/default.nix-
pkgs/development/python-modules/zope-proxy/default.nix-  # circular deps
pkgs/development/python-modules/zope-proxy/default.nix-  doCheck = false;
pkgs/development/python-modules/zope-proxy/default.nix-
--
--
pkgs/development/python-modules/qutip/default.nix-    owner = "qutip";
pkgs/development/python-modules/qutip/default.nix-    repo = "qutip";
pkgs/development/python-modules/qutip/default.nix-    tag = "v${version}";
pkgs/development/python-modules/qutip/default.nix-    hash = "sha256-jH/kpiR0cTIJraMU/ddZe7xX3CMYIV93oyfHfaKxif4=";
pkgs/development/python-modules/qutip/default.nix-  };
pkgs/development/python-modules/qutip/default.nix-
pkgs/development/python-modules/qutip/default.nix-  postPatch =
pkgs/development/python-modules/qutip/default.nix-    # build-time constraint, used to ensure forward and backward compat
pkgs/development/python-modules/qutip/default.nix-    ''
pkgs/development/python-modules/qutip/default.nix:      substituteInPlace pyproject.toml setup.cfg \
pkgs/development/python-modules/qutip/default.nix-        --replace-fail "numpy>=2.0.0" "numpy"
pkgs/development/python-modules/qutip/default.nix-    '';
pkgs/development/python-modules/qutip/default.nix-
pkgs/development/python-modules/qutip/default.nix-  build-system = [
pkgs/development/python-modules/qutip/default.nix-    cython
pkgs/development/python-modules/qutip/default.nix-    oldest-supported-numpy
pkgs/development/python-modules/qutip/default.nix-    setuptools
pkgs/development/python-modules/qutip/default.nix-  ];
pkgs/development/python-modules/qutip/default.nix-
pkgs/development/python-modules/qutip/default.nix-  dependencies = [
--
--
pkgs/development/python-modules/zope-size/default.nix-
pkgs/development/python-modules/zope-size/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/zope-size/default.nix-    owner = "zopefoundation";
pkgs/development/python-modules/zope-size/default.nix-    repo = "zope.size";
pkgs/development/python-modules/zope-size/default.nix-    tag = version;
pkgs/development/python-modules/zope-size/default.nix-    hash = "sha256-9r7l3RgE9gvxJ2I5rFvNn/XIztecXW3GseGeM3MzfTU=";
pkgs/development/python-modules/zope-size/default.nix-  };
pkgs/development/python-modules/zope-size/default.nix-
pkgs/development/python-modules/zope-size/default.nix-  postPatch = ''
pkgs/development/python-modules/zope-size/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/zope-size/default.nix-      --replace-fail "setuptools <= 75.6.0" setuptools
pkgs/development/python-modules/zope-size/default.nix-  '';
pkgs/development/python-modules/zope-size/default.nix-
pkgs/development/python-modules/zope-size/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/zope-size/default.nix-
pkgs/development/python-modules/zope-size/default.nix-  dependencies = [
pkgs/development/python-modules/zope-size/default.nix-    zope-i18nmessageid
pkgs/development/python-modules/zope-size/default.nix-    zope-interface
pkgs/development/python-modules/zope-size/default.nix-  ];
pkgs/development/python-modules/zope-size/default.nix-
--
--
pkgs/development/python-modules/tox/default.nix-
pkgs/development/python-modules/tox/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/tox/default.nix-    owner = "tox-dev";
pkgs/development/python-modules/tox/default.nix-    repo = "tox";
pkgs/development/python-modules/tox/default.nix-    tag = version;
pkgs/development/python-modules/tox/default.nix-    hash = "sha256-EKJsFf4LvfDi3OL6iNhKEBl5zlpdLET9RkfHEP7E9xU=";
pkgs/development/python-modules/tox/default.nix-  };
pkgs/development/python-modules/tox/default.nix-
pkgs/development/python-modules/tox/default.nix-  postPatch = ''
pkgs/development/python-modules/tox/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/tox/default.nix-      --replace "packaging>=22" "packaging"
pkgs/development/python-modules/tox/default.nix-  '';
pkgs/development/python-modules/tox/default.nix-
pkgs/development/python-modules/tox/default.nix-  nativeBuildInputs = [
pkgs/development/python-modules/tox/default.nix-    hatchling
pkgs/development/python-modules/tox/default.nix-    hatch-vcs
pkgs/development/python-modules/tox/default.nix-  ];
pkgs/development/python-modules/tox/default.nix-
pkgs/development/python-modules/tox/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/tox/default.nix-    cachetools
--
--
pkgs/development/python-modules/duckdb/default.nix-    # we can't use sourceRoot otherwise patches don't apply, because the patches apply to the C++ library
pkgs/development/python-modules/duckdb/default.nix-    cd tools/pythonpkg
pkgs/development/python-modules/duckdb/default.nix-
pkgs/development/python-modules/duckdb/default.nix-    # 1. let nix control build cores
pkgs/development/python-modules/duckdb/default.nix-    # 2. default to extension autoload & autoinstall disabled
pkgs/development/python-modules/duckdb/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/duckdb/default.nix-      --replace-fail "ParallelCompile()" 'ParallelCompile("NIX_BUILD_CORES")' \
pkgs/development/python-modules/duckdb/default.nix-      --replace-fail "define_macros.extend([('DUCKDB_EXTENSION_AUTOLOAD_DEFAULT', '1'), ('DUCKDB_EXTENSION_AUTOINSTALL_DEFAULT', '1')])" "pass"
pkgs/development/python-modules/duckdb/default.nix-
pkgs/development/python-modules/duckdb/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/duckdb/default.nix-      --replace-fail 'setuptools_scm>=6.4,<8.0' 'setuptools_scm'
pkgs/development/python-modules/duckdb/default.nix-  '';
pkgs/development/python-modules/duckdb/default.nix-
pkgs/development/python-modules/duckdb/default.nix-  env = {
pkgs/development/python-modules/duckdb/default.nix-    DUCKDB_BUILD_UNITY = 1;
pkgs/development/python-modules/duckdb/default.nix-    OVERRIDE_GIT_DESCRIBE = "v${version}-0-g${rev}";
pkgs/development/python-modules/duckdb/default.nix-  };
pkgs/development/python-modules/duckdb/default.nix-
pkgs/development/python-modules/duckdb/default.nix-  build-system = [
pkgs/development/python-modules/duckdb/default.nix-    pybind11
--
--
pkgs/development/python-modules/aiooncue/default.nix-
pkgs/development/python-modules/aiooncue/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/aiooncue/default.nix-    owner = "bdraco";
pkgs/development/python-modules/aiooncue/default.nix-    repo = "aiooncue";
pkgs/development/python-modules/aiooncue/default.nix-    tag = version;
pkgs/development/python-modules/aiooncue/default.nix-    hash = "sha256-0Cdt/rUsl4OMLUTSC8WJXEiwzrhyn7JJIcVE/55LlgU=";
pkgs/development/python-modules/aiooncue/default.nix-  };
pkgs/development/python-modules/aiooncue/default.nix-
pkgs/development/python-modules/aiooncue/default.nix-  postPatch = ''
pkgs/development/python-modules/aiooncue/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/aiooncue/default.nix-      --replace '"setuptools>=75.8.0"' ""
pkgs/development/python-modules/aiooncue/default.nix-  '';
pkgs/development/python-modules/aiooncue/default.nix-
pkgs/development/python-modules/aiooncue/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/aiooncue/default.nix-
pkgs/development/python-modules/aiooncue/default.nix-  dependencies = [ aiohttp ];
pkgs/development/python-modules/aiooncue/default.nix-
pkgs/development/python-modules/aiooncue/default.nix-  # Tests are out-dated
pkgs/development/python-modules/aiooncue/default.nix-  doCheck = false;
pkgs/development/python-modules/aiooncue/default.nix-
--
--
pkgs/development/python-modules/name-that-hash/default.nix-
pkgs/development/python-modules/name-that-hash/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/name-that-hash/default.nix-    owner = "HashPals";
pkgs/development/python-modules/name-that-hash/default.nix-    repo = "name-that-hash";
pkgs/development/python-modules/name-that-hash/default.nix-    rev = version;
pkgs/development/python-modules/name-that-hash/default.nix-    hash = "sha256-zOb4BS3zG1x8GLXAooqqvMOw0fNbw35JuRWOdGP26/8=";
pkgs/development/python-modules/name-that-hash/default.nix-  };
pkgs/development/python-modules/name-that-hash/default.nix-
pkgs/development/python-modules/name-that-hash/default.nix-  # TODO remove on next update which bumps rich
pkgs/development/python-modules/name-that-hash/default.nix-  postPatch = ''
pkgs/development/python-modules/name-that-hash/default.nix:    substituteInPlace pyproject.toml --replace 'rich = ">=9.9,<11.0"' 'rich = ">=9.9"'
pkgs/development/python-modules/name-that-hash/default.nix-  '';
pkgs/development/python-modules/name-that-hash/default.nix-
pkgs/development/python-modules/name-that-hash/default.nix-  nativeBuildInputs = [ poetry-core ];
pkgs/development/python-modules/name-that-hash/default.nix-
pkgs/development/python-modules/name-that-hash/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/name-that-hash/default.nix-    click
pkgs/development/python-modules/name-that-hash/default.nix-    rich
pkgs/development/python-modules/name-that-hash/default.nix-  ];
pkgs/development/python-modules/name-that-hash/default.nix-
pkgs/development/python-modules/name-that-hash/default.nix-  pythonImportsCheck = [ "name_that_hash" ];
--
pkgs/development/python-modules/qiskit-ibmq-provider/default.nix-    nest-asyncio
pkgs/development/python-modules/qiskit-ibmq-provider/default.nix-    qiskit-terra
pkgs/development/python-modules/qiskit-ibmq-provider/default.nix-    requests
pkgs/development/python-modules/qiskit-ibmq-provider/default.nix-    requests-ntlm
pkgs/development/python-modules/qiskit-ibmq-provider/default.nix-    websocket-client
pkgs/development/python-modules/qiskit-ibmq-provider/default.nix-    websockets
pkgs/development/python-modules/qiskit-ibmq-provider/default.nix-  ]
pkgs/development/python-modules/qiskit-ibmq-provider/default.nix-  ++ lib.optionals withVisualization visualizationPackages;
pkgs/development/python-modules/qiskit-ibmq-provider/default.nix-
pkgs/development/python-modules/qiskit-ibmq-provider/default.nix-  postPatch = ''
pkgs/development/python-modules/qiskit-ibmq-provider/default.nix:    substituteInPlace setup.py --replace "websocket-client>=1.0.1" "websocket-client"
pkgs/development/python-modules/qiskit-ibmq-provider/default.nix-  '';
pkgs/development/python-modules/qiskit-ibmq-provider/default.nix-
pkgs/development/python-modules/qiskit-ibmq-provider/default.nix-  # Most tests require credentials to run on IBMQ
pkgs/development/python-modules/qiskit-ibmq-provider/default.nix-  nativeCheckInputs = [
pkgs/development/python-modules/qiskit-ibmq-provider/default.nix-    pytestCheckHook
pkgs/development/python-modules/qiskit-ibmq-provider/default.nix-    nbconvert
pkgs/development/python-modules/qiskit-ibmq-provider/default.nix-    nbformat
pkgs/development/python-modules/qiskit-ibmq-provider/default.nix-    pproxy
pkgs/development/python-modules/qiskit-ibmq-provider/default.nix-    qiskit-aer
pkgs/development/python-modules/qiskit-ibmq-provider/default.nix-    vcrpy
--
pkgs/development/python-modules/envoy-reader/default.nix-    pytest-raises
pkgs/development/python-modules/envoy-reader/default.nix-    pytest-asyncio
pkgs/development/python-modules/envoy-reader/default.nix-    pytestCheckHook
pkgs/development/python-modules/envoy-reader/default.nix-    respx
pkgs/development/python-modules/envoy-reader/default.nix-  ];
pkgs/development/python-modules/envoy-reader/default.nix-
pkgs/development/python-modules/envoy-reader/default.nix-  pythonRelaxDeps = [ "pyjwt" ];
pkgs/development/python-modules/envoy-reader/default.nix-
pkgs/development/python-modules/envoy-reader/default.nix-  postPatch = ''
pkgs/development/python-modules/envoy-reader/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/envoy-reader/default.nix-      --replace-fail "pytest-runner>=5.2" ""
pkgs/development/python-modules/envoy-reader/default.nix-  '';
pkgs/development/python-modules/envoy-reader/default.nix-
pkgs/development/python-modules/envoy-reader/default.nix-  pythonImportsCheck = [ "envoy_reader" ];
pkgs/development/python-modules/envoy-reader/default.nix-
pkgs/development/python-modules/envoy-reader/default.nix-  meta = with lib; {
pkgs/development/python-modules/envoy-reader/default.nix-    description = "Python module to read from Enphase Envoy units";
pkgs/development/python-modules/envoy-reader/default.nix-    homepage = "https://github.com/jesserizzo/envoy_reader";
pkgs/development/python-modules/envoy-reader/default.nix-    license = licenses.mit;
pkgs/development/python-modules/envoy-reader/default.nix-    maintainers = with maintainers; [ fab ];
--
--
pkgs/development/python-modules/netbox-napalm-plugin/default.nix-
pkgs/development/python-modules/netbox-napalm-plugin/default.nix-  dependencies = [ napalm ];
pkgs/development/python-modules/netbox-napalm-plugin/default.nix-
pkgs/development/python-modules/netbox-napalm-plugin/default.nix-  nativeCheckInputs = [
pkgs/development/python-modules/netbox-napalm-plugin/default.nix-    netbox
pkgs/development/python-modules/netbox-napalm-plugin/default.nix-    django
pkgs/development/python-modules/netbox-napalm-plugin/default.nix-  ];
pkgs/development/python-modules/netbox-napalm-plugin/default.nix-
pkgs/development/python-modules/netbox-napalm-plugin/default.nix-  postPatch = ''
pkgs/development/python-modules/netbox-napalm-plugin/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/netbox-napalm-plugin/default.nix-      --replace-fail 'napalm<5.0' 'napalm'
pkgs/development/python-modules/netbox-napalm-plugin/default.nix-  '';
pkgs/development/python-modules/netbox-napalm-plugin/default.nix-
pkgs/development/python-modules/netbox-napalm-plugin/default.nix-  preFixup = ''
pkgs/development/python-modules/netbox-napalm-plugin/default.nix-    export PYTHONPATH=${netbox}/opt/netbox/netbox:$PYTHONPATH
pkgs/development/python-modules/netbox-napalm-plugin/default.nix-  '';
pkgs/development/python-modules/netbox-napalm-plugin/default.nix-
pkgs/development/python-modules/netbox-napalm-plugin/default.nix-  pythonImportsCheck = [ "netbox_napalm_plugin" ];
pkgs/development/python-modules/netbox-napalm-plugin/default.nix-
pkgs/development/python-modules/netbox-napalm-plugin/default.nix-  meta = {
--
--
pkgs/development/python-modules/pygame-ce/default.nix-    })
pkgs/development/python-modules/pygame-ce/default.nix-    # https://github.com/libsdl-org/sdl2-compat/issues/476
pkgs/development/python-modules/pygame-ce/default.nix-    ./skip-rle-tests.patch
pkgs/development/python-modules/pygame-ce/default.nix-  ];
pkgs/development/python-modules/pygame-ce/default.nix-
pkgs/development/python-modules/pygame-ce/default.nix-  postPatch = ''
pkgs/development/python-modules/pygame-ce/default.nix-    # "pyproject-metadata!=0.9.1" was pinned due to https://github.com/pygame-community/pygame-ce/pull/3395
pkgs/development/python-modules/pygame-ce/default.nix-    # cython was pinned to fix windows build hangs (pygame-community/pygame-ce/pull/3015)
pkgs/development/python-modules/pygame-ce/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/pygame-ce/default.nix-      --replace-fail '"pyproject-metadata!=0.9.1",' '"pyproject-metadata",' \
pkgs/development/python-modules/pygame-ce/default.nix-      --replace-fail '"meson<=1.7.0",' '"meson",' \
pkgs/development/python-modules/pygame-ce/default.nix-      --replace-fail '"meson-python<=0.17.1",' '"meson-python",' \
pkgs/development/python-modules/pygame-ce/default.nix-      --replace-fail '"ninja<=1.12.1",' "" \
pkgs/development/python-modules/pygame-ce/default.nix-      --replace-fail '"cython<=3.0.11",' '"cython",' \
pkgs/development/python-modules/pygame-ce/default.nix-      --replace-fail '"sphinx<=8.1.3",' "" \
pkgs/development/python-modules/pygame-ce/default.nix-      --replace-fail '"sphinx-autoapi<=3.3.2",' ""
pkgs/development/python-modules/pygame-ce/default.nix:    substituteInPlace buildconfig/config_{unix,darwin}.py \
pkgs/development/python-modules/pygame-ce/default.nix-      --replace-fail 'from distutils' 'from setuptools._distutils'
pkgs/development/python-modules/pygame-ce/default.nix:    substituteInPlace src_py/sysfont.py \
pkgs/development/python-modules/pygame-ce/default.nix-      --replace-fail 'path="fc-list"' 'path="${fontconfig}/bin/fc-list"' \
pkgs/development/python-modules/pygame-ce/default.nix-      --replace-fail /usr/X11/bin/fc-list ${fontconfig}/bin/fc-list
pkgs/development/python-modules/pygame-ce/default.nix-  ''
pkgs/development/python-modules/pygame-ce/default.nix-  + lib.optionalString stdenv.hostPlatform.isDarwin ''
pkgs/development/python-modules/pygame-ce/default.nix-    # flaky
pkgs/development/python-modules/pygame-ce/default.nix-    rm test/system_test.py
pkgs/development/python-modules/pygame-ce/default.nix:    substituteInPlace test/meson.build \
--
pkgs/development/python-modules/tbm-utils/default.nix-    })
pkgs/development/python-modules/tbm-utils/default.nix-    (fetchpatch {
pkgs/development/python-modules/tbm-utils/default.nix-      name = "update-testsupport-pendulum-3.patch";
pkgs/development/python-modules/tbm-utils/default.nix-      url = "https://github.com/thebigmunch/tbm-utils/commit/a0331d0c15f11cd26bfbb42eebd17296167161ed.patch";
pkgs/development/python-modules/tbm-utils/default.nix-      hash = "sha256-KG6yfnnBltavbNvIBTdbK+CPXwZTLYl14925RY2a8vs=";
pkgs/development/python-modules/tbm-utils/default.nix-    })
pkgs/development/python-modules/tbm-utils/default.nix-  ];
pkgs/development/python-modules/tbm-utils/default.nix-
pkgs/development/python-modules/tbm-utils/default.nix-  postPatch = ''
pkgs/development/python-modules/tbm-utils/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/tbm-utils/default.nix-      --replace-fail 'poetry>=1.0.0' 'poetry-core' \
pkgs/development/python-modules/tbm-utils/default.nix-      --replace-fail 'poetry.masonry.api' 'poetry.core.masonry.api'
pkgs/development/python-modules/tbm-utils/default.nix-  '';
pkgs/development/python-modules/tbm-utils/default.nix-
pkgs/development/python-modules/tbm-utils/default.nix-  pythonRelaxDeps = [ "attrs" ];
pkgs/development/python-modules/tbm-utils/default.nix-
pkgs/development/python-modules/tbm-utils/default.nix-  build-system = [ poetry-core ];
pkgs/development/python-modules/tbm-utils/default.nix-
pkgs/development/python-modules/tbm-utils/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/tbm-utils/default.nix-    attrs
--
--
pkgs/development/python-modules/pyprecice/default.nix-
pkgs/development/python-modules/pyprecice/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/pyprecice/default.nix-    owner = "precice";
pkgs/development/python-modules/pyprecice/default.nix-    repo = "python-bindings";
pkgs/development/python-modules/pyprecice/default.nix-    tag = "v${version}";
pkgs/development/python-modules/pyprecice/default.nix-    hash = "sha256-8AM2wbPX54UaMO4MzLOV0TljLTAPOqR9gUbtT2McNjs=";
pkgs/development/python-modules/pyprecice/default.nix-  };
pkgs/development/python-modules/pyprecice/default.nix-
pkgs/development/python-modules/pyprecice/default.nix-  postPatch = ''
pkgs/development/python-modules/pyprecice/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/pyprecice/default.nix-      --replace-fail "setuptools>=61,<72" "setuptools"
pkgs/development/python-modules/pyprecice/default.nix-  '';
pkgs/development/python-modules/pyprecice/default.nix-
pkgs/development/python-modules/pyprecice/default.nix-  build-system = [
pkgs/development/python-modules/pyprecice/default.nix-    cython
pkgs/development/python-modules/pyprecice/default.nix-    pip
pkgs/development/python-modules/pyprecice/default.nix-    pkgconfig
pkgs/development/python-modules/pyprecice/default.nix-    setuptools
pkgs/development/python-modules/pyprecice/default.nix-  ];
pkgs/development/python-modules/pyprecice/default.nix-
--
--
pkgs/development/python-modules/cheroot/default.nix-    inherit pname version;
pkgs/development/python-modules/cheroot/default.nix-    hash = "sha256-4LgveXZY0muGE+yOtWPDsI5r1qeSHp1Qib0Rda0bF0A=";
pkgs/development/python-modules/cheroot/default.nix-  };
pkgs/development/python-modules/cheroot/default.nix-
pkgs/development/python-modules/cheroot/default.nix-  # remove setuptools-scm-git-archive dependency
pkgs/development/python-modules/cheroot/default.nix-  # https://github.com/cherrypy/cheroot/commit/f0c51af263e20f332c6f675aa90ec6705ae4f5d1
pkgs/development/python-modules/cheroot/default.nix-  # there is a difference between the github source and the pypi tarball source,
pkgs/development/python-modules/cheroot/default.nix-  # and it is not easy to apply patches.
pkgs/development/python-modules/cheroot/default.nix-  postPatch = ''
pkgs/development/python-modules/cheroot/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/cheroot/default.nix-      --replace '"setuptools_scm_git_archive>=1.1",' ""
pkgs/development/python-modules/cheroot/default.nix:    substituteInPlace setup.cfg \
pkgs/development/python-modules/cheroot/default.nix-      --replace "setuptools_scm_git_archive>=1.0" ""
pkgs/development/python-modules/cheroot/default.nix-  '';
pkgs/development/python-modules/cheroot/default.nix-
pkgs/development/python-modules/cheroot/default.nix-  nativeBuildInputs = [ setuptools-scm ];
pkgs/development/python-modules/cheroot/default.nix-
pkgs/development/python-modules/cheroot/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/cheroot/default.nix-    jaraco-functools
pkgs/development/python-modules/cheroot/default.nix-    more-itertools
pkgs/development/python-modules/cheroot/default.nix-    six
pkgs/development/python-modules/cheroot/default.nix-  ];
--
--
pkgs/development/python-modules/clickhouse-driver/default.nix-
pkgs/development/python-modules/clickhouse-driver/default.nix-  nativeCheckInputs = [
pkgs/development/python-modules/clickhouse-driver/default.nix-    freezegun
pkgs/development/python-modules/clickhouse-driver/default.nix-    mock
pkgs/development/python-modules/clickhouse-driver/default.nix-    pytest-xdist
pkgs/development/python-modules/clickhouse-driver/default.nix-    pytestCheckHook
pkgs/development/python-modules/clickhouse-driver/default.nix-  ];
pkgs/development/python-modules/clickhouse-driver/default.nix-
pkgs/development/python-modules/clickhouse-driver/default.nix-  postPatch = ''
pkgs/development/python-modules/clickhouse-driver/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/clickhouse-driver/default.nix-      --replace "lz4<=3.0.1" "lz4<=4"
pkgs/development/python-modules/clickhouse-driver/default.nix-  '';
pkgs/development/python-modules/clickhouse-driver/default.nix-
pkgs/development/python-modules/clickhouse-driver/default.nix-  # remove source to prevent pytest testing source instead of the build artifacts
pkgs/development/python-modules/clickhouse-driver/default.nix-  # (the source doesn't contain the extension modules)
pkgs/development/python-modules/clickhouse-driver/default.nix-  preCheck = ''
pkgs/development/python-modules/clickhouse-driver/default.nix-    rm -rf clickhouse_driver
pkgs/development/python-modules/clickhouse-driver/default.nix-  '';
pkgs/development/python-modules/clickhouse-driver/default.nix-
pkgs/development/python-modules/clickhouse-driver/default.nix-  # some test in test_buffered_reader.py doesn't seem to return
--
--
pkgs/development/python-modules/dmgbuild/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/dmgbuild/default.nix-    owner = "dmgbuild";
pkgs/development/python-modules/dmgbuild/default.nix-    repo = "dmgbuild";
pkgs/development/python-modules/dmgbuild/default.nix-    rev = "refs/tags/v${version}";
pkgs/development/python-modules/dmgbuild/default.nix-    hash = "sha256-PozYxmXumFnptIgb4FM4b/Q5tx0MIS2bVw2kCuGucA8=";
pkgs/development/python-modules/dmgbuild/default.nix-  };
pkgs/development/python-modules/dmgbuild/default.nix-
pkgs/development/python-modules/dmgbuild/default.nix-  postPatch = ''
pkgs/development/python-modules/dmgbuild/default.nix-    # relax all deps
pkgs/development/python-modules/dmgbuild/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/dmgbuild/default.nix-      --replace-fail "==" ">="
pkgs/development/python-modules/dmgbuild/default.nix-  '';
pkgs/development/python-modules/dmgbuild/default.nix-
pkgs/development/python-modules/dmgbuild/default.nix-  build-system = [
pkgs/development/python-modules/dmgbuild/default.nix-    setuptools
pkgs/development/python-modules/dmgbuild/default.nix-  ];
pkgs/development/python-modules/dmgbuild/default.nix-
pkgs/development/python-modules/dmgbuild/default.nix-  dependencies = [
pkgs/development/python-modules/dmgbuild/default.nix-    ds-store
pkgs/development/python-modules/dmgbuild/default.nix-    importlib-resources
--
pkgs/development/python-modules/batchspawner/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/batchspawner/default.nix-    owner = "jupyterhub";
pkgs/development/python-modules/batchspawner/default.nix-    repo = "batchspawner";
pkgs/development/python-modules/batchspawner/default.nix-    tag = "v${version}";
pkgs/development/python-modules/batchspawner/default.nix-    hash = "sha256-Z7kB8b7s11wokTachLI/N+bdUV+FfCRTemL1KYQpzio=";
pkgs/development/python-modules/batchspawner/default.nix-  };
pkgs/development/python-modules/batchspawner/default.nix-
pkgs/development/python-modules/batchspawner/default.nix-  # When using pytest-asyncio>=0.24, jupyterhub no longer re-defines the event_loop function in its
pkgs/development/python-modules/batchspawner/default.nix-  # conftest.py, so it cannot be imported from there.
pkgs/development/python-modules/batchspawner/default.nix-  postPatch = ''
pkgs/development/python-modules/batchspawner/default.nix:    substituteInPlace batchspawner/tests/conftest.py \
pkgs/development/python-modules/batchspawner/default.nix-      --replace-fail \
pkgs/development/python-modules/batchspawner/default.nix-        "from jupyterhub.tests.conftest import db, event_loop  # noqa" \
pkgs/development/python-modules/batchspawner/default.nix-        "from jupyterhub.tests.conftest import db"
pkgs/development/python-modules/batchspawner/default.nix-  '';
pkgs/development/python-modules/batchspawner/default.nix-
pkgs/development/python-modules/batchspawner/default.nix-  build-system = [
pkgs/development/python-modules/batchspawner/default.nix-    setuptools
--
pkgs/development/python-modules/timing-asgi/default.nix-    repo = "timing-asgi";
pkgs/development/python-modules/timing-asgi/default.nix-    tag = "v${version}";
pkgs/development/python-modules/timing-asgi/default.nix-    hash = "sha256-oEDesmy9t2m51Zd6Zg87qoYbfbDnejfrbjyBkZ3hF58=";
pkgs/development/python-modules/timing-asgi/default.nix-  };
pkgs/development/python-modules/timing-asgi/default.nix-
pkgs/development/python-modules/timing-asgi/default.nix-  # The current pyproject.toml content is not compatible with poetry-core==2.0
pkgs/development/python-modules/timing-asgi/default.nix-  postPatch = ''
pkgs/development/python-modules/timing-asgi/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/timing-asgi/default.nix-      --replace-fail "[tool.poetry]" "[project]" \
pkgs/development/python-modules/timing-asgi/default.nix-      --replace-fail \
pkgs/development/python-modules/timing-asgi/default.nix-        '"Steinn Eldjárn Sigurðarson <steinnes@gmail.com>"' \
pkgs/development/python-modules/timing-asgi/default.nix-        '{ name = "Steinn Eldjárn Sigurðarson", email = "steinnes@gmail.com" },' \
pkgs/development/python-modules/timing-asgi/default.nix-      --replace-fail poetry.masonry.api poetry.core.masonry.api \
pkgs/development/python-modules/timing-asgi/default.nix-      --replace-fail "poetry>=" "poetry-core>="
pkgs/development/python-modules/timing-asgi/default.nix-  '';
pkgs/development/python-modules/timing-asgi/default.nix-
pkgs/development/python-modules/timing-asgi/default.nix-  build-system = [ poetry-core ];
pkgs/development/python-modules/timing-asgi/default.nix-
--
pkgs/development/python-modules/sphinx-autodoc2/default.nix-    astroid
pkgs/development/python-modules/sphinx-autodoc2/default.nix-    typing-extensions
pkgs/development/python-modules/sphinx-autodoc2/default.nix-
pkgs/development/python-modules/sphinx-autodoc2/default.nix-    # cli deps
pkgs/development/python-modules/sphinx-autodoc2/default.nix-    typer
--
pkgs/development/python-modules/mongoengine/default.nix-  nativeCheckInputs = [
pkgs/development/python-modules/mongoengine/default.nix-    pytestCheckHook
pkgs/development/python-modules/mongoengine/default.nix-    pillow
pkgs/development/python-modules/mongoengine/default.nix-    coverage
pkgs/development/python-modules/mongoengine/default.nix-    blinker
pkgs/development/python-modules/mongoengine/default.nix-  ];
pkgs/development/python-modules/mongoengine/default.nix-
pkgs/development/python-modules/mongoengine/default.nix-  postPatch = ''
pkgs/development/python-modules/mongoengine/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/mongoengine/default.nix-      --replace "coverage==4.2" "coverage" \
pkgs/development/python-modules/mongoengine/default.nix-      --replace "pymongo>=3.4,<=4.0" "pymongo"
pkgs/development/python-modules/mongoengine/default.nix-  '';
pkgs/development/python-modules/mongoengine/default.nix-
pkgs/development/python-modules/mongoengine/default.nix-  # tests require mongodb running in background
pkgs/development/python-modules/mongoengine/default.nix-  doCheck = false;
pkgs/development/python-modules/mongoengine/default.nix-
pkgs/development/python-modules/mongoengine/default.nix-  pythonImportsCheck = [ "mongoengine" ];
pkgs/development/python-modules/mongoengine/default.nix-
pkgs/development/python-modules/mongoengine/default.nix-  meta = with lib; {
--
pkgs/development/python-modules/python-sat/default.nix-  src = fetchFromGitHub {
--
pkgs/development/python-modules/craft-application/default.nix-    "requests"
pkgs/development/python-modules/craft-application/default.nix-  ];
pkgs/development/python-modules/craft-application/default.nix-
--
pkgs/development/python-modules/craft-application/default.nix-  ];
pkgs/development/python-modules/craft-application/default.nix-
pkgs/development/python-modules/craft-application/default.nix-  preCheck = ''
pkgs/development/python-modules/craft-application/default.nix-    # Tests require access to /etc/os-release, which isn't accessible in
pkgs/development/python-modules/craft-application/default.nix-    # the test environment, so create a fake file, and modify the code
pkgs/development/python-modules/craft-application/default.nix-    # to look for it.
pkgs/development/python-modules/craft-application/default.nix-    echo 'ID=nixos' > $HOME/os-release
pkgs/development/python-modules/craft-application/default.nix-    echo 'NAME=NixOS' >> $HOME/os-release
pkgs/development/python-modules/craft-application/default.nix-    echo 'VERSION_ID="24.05"' >> $HOME/os-release
pkgs/development/python-modules/craft-application/default.nix-
pkgs/development/python-modules/craft-application/default.nix:    substituteInPlace craft_application/util/platforms.py \
pkgs/development/python-modules/craft-application/default.nix-      --replace-fail "os_utils.OsRelease()" "os_utils.OsRelease(os_release_file='$HOME/os-release')"
pkgs/development/python-modules/craft-application/default.nix-
pkgs/development/python-modules/craft-application/default.nix-    # Not using `--replace-fail` here only because it simplifies overriding this package in the charmcraft
pkgs/development/python-modules/craft-application/default.nix-    # derivation. Once charmcraft has moved to craft-application >= 5, `--replace-fail` can be added.
pkgs/development/python-modules/craft-application/default.nix:    substituteInPlace tests/conftest.py \
pkgs/development/python-modules/craft-application/default.nix-      --replace "include_lsb=False, include_uname=False, include_oslevel=False" "include_lsb=False, include_uname=False, include_oslevel=False, os_release_file='$HOME/os-release'"
pkgs/development/python-modules/craft-application/default.nix-
pkgs/development/python-modules/craft-application/default.nix-    # The project attempts to write into the user's runtime directory, usually
pkgs/development/python-modules/craft-application/default.nix-    # '/run/user/<uid>', which fails in the build environment. By setting this
pkgs/development/python-modules/craft-application/default.nix-    # variable, we redirect the runtime directory lookup to the temp directory
pkgs/development/python-modules/craft-application/default.nix-    # created by the 'writableTmpDirAsHomeHook'.
pkgs/development/python-modules/craft-application/default.nix-    export XDG_RUNTIME_DIR="$HOME"
pkgs/development/python-modules/craft-application/default.nix-  '';
pkgs/development/python-modules/craft-application/default.nix-
pkgs/development/python-modules/craft-application/default.nix-  pythonImportsCheck = [ "craft_application" ];
--
pkgs/development/python-modules/music-assistant-client/default.nix-  pyproject = true;
pkgs/development/python-modules/music-assistant-client/default.nix-
pkgs/development/python-modules/music-assistant-client/default.nix-  src = fetchFromGitHub {
--
pkgs/development/python-modules/oldest-supported-numpy/default.nix-  };
pkgs/development/python-modules/oldest-supported-numpy/default.nix-
pkgs/development/python-modules/oldest-supported-numpy/default.nix-  # The purpose of oldest-supported-numpy is to build a project against the
pkgs/development/python-modules/oldest-supported-numpy/default.nix-  # oldest version of numpy for a given Python distribution in order to build
pkgs/development/python-modules/oldest-supported-numpy/default.nix-  # a binary that is compatible with the largest possible versions of numpy.
pkgs/development/python-modules/oldest-supported-numpy/default.nix-  # We only build against one version of numpy in nixpkgs, so instead we only
pkgs/development/python-modules/oldest-supported-numpy/default.nix-  # want to make sure that we have a version above the minimum.
pkgs/development/python-modules/oldest-supported-numpy/default.nix-  #
pkgs/development/python-modules/oldest-supported-numpy/default.nix-  postPatch = ''
pkgs/development/python-modules/oldest-supported-numpy/default.nix:    substituteInPlace setup.cfg \
pkgs/development/python-modules/oldest-supported-numpy/default.nix-      --replace 'numpy==' 'numpy>='
pkgs/development/python-modules/oldest-supported-numpy/default.nix-  '';
pkgs/development/python-modules/oldest-supported-numpy/default.nix-
pkgs/development/python-modules/oldest-supported-numpy/default.nix-  propagatedBuildInputs = [ numpy ];
pkgs/development/python-modules/oldest-supported-numpy/default.nix-
pkgs/development/python-modules/oldest-supported-numpy/default.nix-  # package has no tests
pkgs/development/python-modules/oldest-supported-numpy/default.nix-  doCheck = false;
pkgs/development/python-modules/oldest-supported-numpy/default.nix-
pkgs/development/python-modules/oldest-supported-numpy/default.nix-  meta = with lib; {
pkgs/development/python-modules/oldest-supported-numpy/default.nix-    description = "Meta-package providing the oldest supported Numpy for a given Python version and platform";
--
--
pkgs/development/python-modules/cx-freeze/default.nix-  };
pkgs/development/python-modules/cx-freeze/default.nix-
pkgs/development/python-modules/cx-freeze/default.nix-  patches = [
pkgs/development/python-modules/cx-freeze/default.nix-    # ValueError: '/nix/store/33ajdw6s479bg0ydhk0zqrxi6p989gbl-python3.12-pytest-8.3.5/lib/python3.12/site-packages'
pkgs/development/python-modules/cx-freeze/default.nix-    # is not in the subpath of '/nix/store/fqm9bqqlmaqqr02qbalm1bazp810qfiw-python3-3.12.9'
pkgs/development/python-modules/cx-freeze/default.nix-    ./fix-tests-relative-path.patch
pkgs/development/python-modules/cx-freeze/default.nix-  ];
pkgs/development/python-modules/cx-freeze/default.nix-
pkgs/development/python-modules/cx-freeze/default.nix-  postPatch = ''
pkgs/development/python-modules/cx-freeze/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/cx-freeze/default.nix-      --replace-fail "setuptools>=77.0.3,<=80.4.0" "setuptools>=77.0.3"
pkgs/development/python-modules/cx-freeze/default.nix-  '';
pkgs/development/python-modules/cx-freeze/default.nix-
pkgs/development/python-modules/cx-freeze/default.nix-  build-system = [
pkgs/development/python-modules/cx-freeze/default.nix-    setuptools
pkgs/development/python-modules/cx-freeze/default.nix-  ];
pkgs/development/python-modules/cx-freeze/default.nix-
pkgs/development/python-modules/cx-freeze/default.nix-  buildInputs = [ ncurses ];
pkgs/development/python-modules/cx-freeze/default.nix-
pkgs/development/python-modules/cx-freeze/default.nix-  pythonRelaxDeps = [ "setuptools" ];
--
--
pkgs/development/python-modules/pandas/default.nix-    # perform this substitution even though python3.pkgs.numpy is of version 2
pkgs/development/python-modules/pandas/default.nix-    # nowadays, because our ecosystem unfortunately doesn't allow easily
pkgs/development/python-modules/pandas/default.nix-    # separating runtime and build-system dependencies. See also:
pkgs/development/python-modules/pandas/default.nix-    #
pkgs/development/python-modules/pandas/default.nix-    # https://discourse.nixos.org/t/several-comments-about-priorities-and-new-policies-in-the-python-ecosystem/51790
pkgs/development/python-modules/pandas/default.nix-    #
pkgs/development/python-modules/pandas/default.nix-    # Being able to build (& run) with Numpy 1 helps for python environments
pkgs/development/python-modules/pandas/default.nix-    # that override globally the `numpy` attribute to point to `numpy_1`.
pkgs/development/python-modules/pandas/default.nix-    postPatch = ''
pkgs/development/python-modules/pandas/default.nix:      substituteInPlace pyproject.toml \
pkgs/development/python-modules/pandas/default.nix-        --replace-fail "numpy>=2.0" numpy
pkgs/development/python-modules/pandas/default.nix-    '';
pkgs/development/python-modules/pandas/default.nix-
pkgs/development/python-modules/pandas/default.nix-    build-system = [
pkgs/development/python-modules/pandas/default.nix-      cython
pkgs/development/python-modules/pandas/default.nix-      meson-python
pkgs/development/python-modules/pandas/default.nix-      meson
pkgs/development/python-modules/pandas/default.nix-      numpy
pkgs/development/python-modules/pandas/default.nix-      pkg-config
pkgs/development/python-modules/pandas/default.nix-      versioneer
--
--
pkgs/development/python-modules/picos/default.nix-
pkgs/development/python-modules/picos/default.nix-  dependencies = [
pkgs/development/python-modules/picos/default.nix-    numpy
pkgs/development/python-modules/picos/default.nix-    cvxopt
pkgs/development/python-modules/picos/default.nix-    scipy
pkgs/development/python-modules/picos/default.nix-  ];
pkgs/development/python-modules/picos/default.nix-
pkgs/development/python-modules/picos/default.nix-  postPatch =
pkgs/development/python-modules/picos/default.nix-    lib.optionalString (pythonOlder "3.12") ''
pkgs/development/python-modules/picos/default.nix:      substituteInPlace picos/modeling/problem.py \
pkgs/development/python-modules/picos/default.nix-        --replace-fail "mappingproxy(OrderedDict({'x': <3×1 Real Variable: x>}))" "mappingproxy(OrderedDict([('x', <3×1 Real Variable: x>)]))"
pkgs/development/python-modules/picos/default.nix-    ''
pkgs/development/python-modules/picos/default.nix-    # TypeError: '<=' not supported between instances of 'ComplexAffineExpression' and 'float'
pkgs/development/python-modules/picos/default.nix-    + lib.optionalString (stdenv.hostPlatform.isDarwin && stdenv.hostPlatform.isAarch64) ''
pkgs/development/python-modules/picos/default.nix-      rm tests/ptest_quantentr.py
pkgs/development/python-modules/picos/default.nix-    '';
pkgs/development/python-modules/picos/default.nix-
pkgs/development/python-modules/picos/default.nix-  checkPhase = ''
pkgs/development/python-modules/picos/default.nix-    runHook preCheck
pkgs/development/python-modules/picos/default.nix-
--
pkgs/development/python-modules/skia-pathops/default.nix-  pyproject = true;
pkgs/development/python-modules/skia-pathops/default.nix-
--
pkgs/development/python-modules/skia-pathops/default.nix:    substituteInPlace src/cpp/skia-builder/skia/gn/skia/BUILD.gn \
pkgs/development/python-modules/skia-pathops/default.nix-      --replace "-march=armv7-a" "-march=armv8-a" \
pkgs/development/python-modules/skia-pathops/default.nix-      --replace "-mfpu=neon" "" \
pkgs/development/python-modules/skia-pathops/default.nix-      --replace "-mthumb" ""
pkgs/development/python-modules/skia-pathops/default.nix:    substituteInPlace src/cpp/skia-builder/skia/src/core/SkOpts.cpp \
pkgs/development/python-modules/skia-pathops/default.nix-      --replace "defined(SK_CPU_ARM64)" "0"
pkgs/development/python-modules/skia-pathops/default.nix-  ''
pkgs/development/python-modules/skia-pathops/default.nix-  +
pkgs/development/python-modules/skia-pathops/default.nix-    lib.optionalString (stdenv.hostPlatform.isDarwin && stdenv.hostPlatform.isx86_64) # old compiler?
pkgs/development/python-modules/skia-pathops/default.nix-      ''
pkgs/development/python-modules/skia-pathops/default.nix-        patch -p1 <<EOF
pkgs/development/python-modules/skia-pathops/default.nix-        --- a/src/cpp/skia-builder/skia/include/private/base/SkTArray.h
pkgs/development/python-modules/skia-pathops/default.nix-        +++ b/src/cpp/skia-builder/skia/include/private/base/SkTArray.h
pkgs/development/python-modules/skia-pathops/default.nix-        @@ -492 +492 @@:
pkgs/development/python-modules/skia-pathops/default.nix-        -    static constexpr int kMaxCapacity = SkToInt(std::min(SIZE_MAX / sizeof(T), (size_t)INT_MAX));
--
pkgs/development/python-modules/zha-quirks/default.nix-  disabled = pythonOlder "3.12";
pkgs/development/python-modules/zha-quirks/default.nix-
pkgs/development/python-modules/zha-quirks/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/zha-quirks/default.nix-    owner = "zigpy";
pkgs/development/python-modules/zha-quirks/default.nix-    repo = "zha-device-handlers";
pkgs/development/python-modules/zha-quirks/default.nix-    tag = version;
pkgs/development/python-modules/zha-quirks/default.nix-    hash = "sha256-txU1KJzQitSR7Y+/18dLo82K0SkPrJ4iQRBX9C4hgGU=";
pkgs/development/python-modules/zha-quirks/default.nix-  };
pkgs/development/python-modules/zha-quirks/default.nix-
pkgs/development/python-modules/zha-quirks/default.nix-  postPatch = ''
pkgs/development/python-modules/zha-quirks/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/zha-quirks/default.nix-      --replace-fail ', "setuptools-git-versioning<2"' "" \
pkgs/development/python-modules/zha-quirks/default.nix-      --replace-fail 'dynamic = ["version"]' 'version = "${version}"'
pkgs/development/python-modules/zha-quirks/default.nix-  '';
pkgs/development/python-modules/zha-quirks/default.nix-
pkgs/development/python-modules/zha-quirks/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/zha-quirks/default.nix-
pkgs/development/python-modules/zha-quirks/default.nix-  dependencies = [
pkgs/development/python-modules/zha-quirks/default.nix-    aiohttp
pkgs/development/python-modules/zha-quirks/default.nix-    zigpy
pkgs/development/python-modules/zha-quirks/default.nix-  ];
--
--
pkgs/development/python-modules/elegy/default.nix-      url = "https://github.com/poets-ai/elegy/commit/0ed472882f470ed9eb7a63b8a537ffabe7e19aa7.patch";
pkgs/development/python-modules/elegy/default.nix-      hash = "sha256-nO/imHo7tEsiZh+64CF/M4eXQ1so3IunVhv8CvYP1ks=";
pkgs/development/python-modules/elegy/default.nix-    })
pkgs/development/python-modules/elegy/default.nix-  ];
pkgs/development/python-modules/elegy/default.nix-
pkgs/development/python-modules/elegy/default.nix-  # The cloudpickle constraint is too strict. wandb is marked as an optional
pkgs/development/python-modules/elegy/default.nix-  # dependency but `buildPythonPackage` doesn't seem to respect that setting.
pkgs/development/python-modules/elegy/default.nix-  # Python constraint: https://github.com/poets-ai/elegy/issues/244
pkgs/development/python-modules/elegy/default.nix-  postPatch = ''
pkgs/development/python-modules/elegy/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/elegy/default.nix-      --replace 'python = ">=3.7,<3.10"' 'python = ">=3.7"' \
pkgs/development/python-modules/elegy/default.nix-      --replace 'cloudpickle = "^1.5.0"' 'cloudpickle = "*"' \
pkgs/development/python-modules/elegy/default.nix-      --replace 'wandb = { version = "^0.12.10", optional = true }' ""
pkgs/development/python-modules/elegy/default.nix-  '';
pkgs/development/python-modules/elegy/default.nix-
pkgs/development/python-modules/elegy/default.nix-  nativeBuildInputs = [ poetry-core ];
pkgs/development/python-modules/elegy/default.nix-
pkgs/development/python-modules/elegy/default.nix-  buildInputs = [ jaxlib ];
pkgs/development/python-modules/elegy/default.nix-
pkgs/development/python-modules/elegy/default.nix-  propagatedBuildInputs = [
--
--
pkgs/development/python-modules/murmurhash/default.nix-
pkgs/development/python-modules/murmurhash/default.nix-  disabled = pythonOlder "3.6";
pkgs/development/python-modules/murmurhash/default.nix-
pkgs/development/python-modules/murmurhash/default.nix-  src = fetchPypi {
pkgs/development/python-modules/murmurhash/default.nix-    inherit pname version;
pkgs/development/python-modules/murmurhash/default.nix-    hash = "sha256-c3JG1B7gD/dLB7C9HwiIvjBNIDzmaOZCyGqmTt4w+Lc=";
pkgs/development/python-modules/murmurhash/default.nix-  };
pkgs/development/python-modules/murmurhash/default.nix-
pkgs/development/python-modules/murmurhash/default.nix-  postPatch = ''
pkgs/development/python-modules/murmurhash/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/murmurhash/default.nix-      --replace "'wheel>=0.32.0,<0.33.0'" ""
pkgs/development/python-modules/murmurhash/default.nix-  '';
pkgs/development/python-modules/murmurhash/default.nix-
pkgs/development/python-modules/murmurhash/default.nix-  buildInputs = [ cython ];
pkgs/development/python-modules/murmurhash/default.nix-
pkgs/development/python-modules/murmurhash/default.nix-  # No test
pkgs/development/python-modules/murmurhash/default.nix-  doCheck = false;
pkgs/development/python-modules/murmurhash/default.nix-
pkgs/development/python-modules/murmurhash/default.nix-  pythonImportsCheck = [ "murmurhash" ];
pkgs/development/python-modules/murmurhash/default.nix-
--
--
pkgs/development/python-modules/btchip-python/default.nix-  format = "setuptools";
pkgs/development/python-modules/btchip-python/default.nix-
pkgs/development/python-modules/btchip-python/default.nix-  src = fetchPypi {
pkgs/development/python-modules/btchip-python/default.nix-    inherit pname version;
pkgs/development/python-modules/btchip-python/default.nix-    hash = "sha256-NPXgwWHAj2XcDQcLov9MMV7SHEt+D6oypGhi0Nwbj1U=";
pkgs/development/python-modules/btchip-python/default.nix-  };
pkgs/development/python-modules/btchip-python/default.nix-
pkgs/development/python-modules/btchip-python/default.nix-  postPatch = ''
pkgs/development/python-modules/btchip-python/default.nix-    # fix extra_requires validation
pkgs/development/python-modules/btchip-python/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/btchip-python/default.nix-      --replace "python-pyscard>=1.6.12-4build1" "python-pyscard>=1.6.12"
pkgs/development/python-modules/btchip-python/default.nix-  '';
pkgs/development/python-modules/btchip-python/default.nix-
pkgs/development/python-modules/btchip-python/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/btchip-python/default.nix-    hidapi
pkgs/development/python-modules/btchip-python/default.nix-    ecdsa
pkgs/development/python-modules/btchip-python/default.nix-  ];
pkgs/development/python-modules/btchip-python/default.nix-
pkgs/development/python-modules/btchip-python/default.nix-  optional-dependencies.smartcard = [ pyscard ];
pkgs/development/python-modules/btchip-python/default.nix-
--
--
pkgs/development/python-modules/avion/default.nix-  disabled = pythonOlder "3.7";
pkgs/development/python-modules/avion/default.nix-
pkgs/development/python-modules/avion/default.nix-  src = fetchPypi {
pkgs/development/python-modules/avion/default.nix-    inherit pname version;
pkgs/development/python-modules/avion/default.nix-    hash = "sha256-v/0NwFmxDZ9kEOx5qs5L9sKzOg/kto79syctg0Ah+30=";
pkgs/development/python-modules/avion/default.nix-  };
pkgs/development/python-modules/avion/default.nix-
pkgs/development/python-modules/avion/default.nix-  postPatch = ''
pkgs/development/python-modules/avion/default.nix-    # https://github.com/mjg59/python-avion/pull/16
pkgs/development/python-modules/avion/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/avion/default.nix-      --replace "bluepy>==1.1.4" "bluepy>=1.1.4"
pkgs/development/python-modules/avion/default.nix-  '';
pkgs/development/python-modules/avion/default.nix-
pkgs/development/python-modules/avion/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/avion/default.nix-    bluepy
pkgs/development/python-modules/avion/default.nix-    csrmesh
pkgs/development/python-modules/avion/default.nix-    pycryptodome
pkgs/development/python-modules/avion/default.nix-    requests
pkgs/development/python-modules/avion/default.nix-  ];
pkgs/development/python-modules/avion/default.nix-
--
--
pkgs/development/python-modules/flux-led/default.nix-
pkgs/development/python-modules/flux-led/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/flux-led/default.nix-    owner = "Danielhiversen";
pkgs/development/python-modules/flux-led/default.nix-    repo = "flux_led";
pkgs/development/python-modules/flux-led/default.nix-    tag = version;
pkgs/development/python-modules/flux-led/default.nix-    hash = "sha256-+i+/WMHdz4HPKDlRPV1Aq9QqrTo5gZiulSc7Hinn+kI=";
pkgs/development/python-modules/flux-led/default.nix-  };
pkgs/development/python-modules/flux-led/default.nix-
pkgs/development/python-modules/flux-led/default.nix-  postPatch = ''
pkgs/development/python-modules/flux-led/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/flux-led/default.nix-      --replace-fail '"pytest-runner>=5.2",' ""
pkgs/development/python-modules/flux-led/default.nix-  '';
pkgs/development/python-modules/flux-led/default.nix-
pkgs/development/python-modules/flux-led/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/flux-led/default.nix-
pkgs/development/python-modules/flux-led/default.nix-  dependencies = [
pkgs/development/python-modules/flux-led/default.nix-    async-timeout
pkgs/development/python-modules/flux-led/default.nix-    webcolors
pkgs/development/python-modules/flux-led/default.nix-  ];
pkgs/development/python-modules/flux-led/default.nix-
--
--
pkgs/development/python-modules/libknot/default.nix-  meta = with lib; {
pkgs/development/python-modules/libknot/default.nix-    description = "Python bindings for libknot";
--
pkgs/development/python-modules/multivolumefile/default.nix-    owner = "miurahr";
pkgs/development/python-modules/multivolumefile/default.nix-    repo = "multivolume";
pkgs/development/python-modules/multivolumefile/default.nix-    tag = "v${version}";
pkgs/development/python-modules/multivolumefile/default.nix-    hash = "sha256-7gjfF7biQZOcph2dfwi2ouDn/uIYik/KBQ0k6u5Ne+Q=";
pkgs/development/python-modules/multivolumefile/default.nix-  };
pkgs/development/python-modules/multivolumefile/default.nix-
pkgs/development/python-modules/multivolumefile/default.nix-  postPatch =
pkgs/development/python-modules/multivolumefile/default.nix-    # Fix typo: `tools` -> `tool`
pkgs/development/python-modules/multivolumefile/default.nix-    # upstream PR: https://codeberg.org/miurahr/multivolume/pulls/9
pkgs/development/python-modules/multivolumefile/default.nix-    ''
pkgs/development/python-modules/multivolumefile/default.nix:      substituteInPlace pyproject.toml \
pkgs/development/python-modules/multivolumefile/default.nix-        --replace-fail 'tools.setuptools_scm' 'tool.setuptools_scm'
pkgs/development/python-modules/multivolumefile/default.nix-    '';
pkgs/development/python-modules/multivolumefile/default.nix-
pkgs/development/python-modules/multivolumefile/default.nix-  build-system = [
pkgs/development/python-modules/multivolumefile/default.nix-    setuptools
pkgs/development/python-modules/multivolumefile/default.nix-    setuptools-scm
pkgs/development/python-modules/multivolumefile/default.nix-  ];
--
pkgs/development/python-modules/mitmproxy-linux/default.nix-      --replace-fail '"+nightly",' "" \
pkgs/development/python-modules/mitmproxy-linux/default.nix-      --replace-fail '"-Z",' "" \
pkgs/development/python-modules/mitmproxy-linux/default.nix-      --replace-fail '"build-std=core",' ""
pkgs/development/python-modules/mitmproxy-linux/default.nix-
pkgs/development/python-modules/mitmproxy-linux/default.nix:    substituteInPlace mitmproxy-linux-ebpf/.cargo/config.toml \
pkgs/development/python-modules/mitmproxy-linux/default.nix-      --replace-fail 'build-std = ["core"]' ""
pkgs/development/python-modules/mitmproxy-linux/default.nix-
pkgs/development/python-modules/mitmproxy-linux/default.nix-    cp ${./fix-mitmproxy-linux-redirector-path.diff} tmp.diff
pkgs/development/python-modules/mitmproxy-linux/default.nix:    substituteInPlace tmp.diff \
pkgs/development/python-modules/mitmproxy-linux/default.nix-      --replace-fail @mitmproxy-linux-redirector@ $out/bin/mitmproxy-linux-redirector
pkgs/development/python-modules/mitmproxy-linux/default.nix-    patch -p1 < tmp.diff
pkgs/development/python-modules/mitmproxy-linux/default.nix-  '';
pkgs/development/python-modules/mitmproxy-linux/default.nix-
pkgs/development/python-modules/mitmproxy-linux/default.nix-  RUSTFLAGS = "-C target-feature=";
pkgs/development/python-modules/mitmproxy-linux/default.nix-  RUSTC_BOOTSTRAP = 1;
pkgs/development/python-modules/mitmproxy-linux/default.nix-
pkgs/development/python-modules/mitmproxy-linux/default.nix-  buildAndTestSubdir = "mitmproxy-linux";
pkgs/development/python-modules/mitmproxy-linux/default.nix-
pkgs/development/python-modules/mitmproxy-linux/default.nix-  nativeBuildInputs = [
--
pkgs/development/python-modules/pyhamcrest/default.nix-  disabled = pythonOlder "3.7";
--
pkgs/development/python-modules/furo/default.nix-  };
pkgs/development/python-modules/furo/default.nix-in
pkgs/development/python-modules/furo/default.nix-
pkgs/development/python-modules/furo/default.nix-buildPythonPackage rec {
pkgs/development/python-modules/furo/default.nix-  inherit pname version src;
pkgs/development/python-modules/furo/default.nix-  pyproject = true;
pkgs/development/python-modules/furo/default.nix-
pkgs/development/python-modules/furo/default.nix-  postPatch = ''
pkgs/development/python-modules/furo/default.nix-    # build with boring backend that does not manage a node env
pkgs/development/python-modules/furo/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/furo/default.nix-      --replace-fail "sphinx-theme-builder >= 0.2.0a10" "flit-core" \
pkgs/development/python-modules/furo/default.nix-      --replace-fail "sphinx_theme_builder" "flit_core.buildapi"
pkgs/development/python-modules/furo/default.nix-
pkgs/development/python-modules/furo/default.nix-    pushd src/furo/theme/furo/static
pkgs/development/python-modules/furo/default.nix-    cp -rv ${web}/{scripts,styles} .
pkgs/development/python-modules/furo/default.nix-    popd
pkgs/development/python-modules/furo/default.nix-  '';
pkgs/development/python-modules/furo/default.nix-
pkgs/development/python-modules/furo/default.nix-  build-system = [ flit-core ];
pkgs/development/python-modules/furo/default.nix-
--
--
pkgs/development/python-modules/habluetooth/default.nix-
pkgs/development/python-modules/habluetooth/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/habluetooth/default.nix-    owner = "Bluetooth-Devices";
pkgs/development/python-modules/habluetooth/default.nix-    repo = "habluetooth";
pkgs/development/python-modules/habluetooth/default.nix-    tag = "v${version}";
pkgs/development/python-modules/habluetooth/default.nix-    hash = "sha256-82eV76oY/exkHbhZt3OaifOoKxN2D6npstvfBDVgszw=";
pkgs/development/python-modules/habluetooth/default.nix-  };
pkgs/development/python-modules/habluetooth/default.nix-
pkgs/development/python-modules/habluetooth/default.nix-  postPatch = ''
pkgs/development/python-modules/habluetooth/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/habluetooth/default.nix-      --replace-fail 'Cython>=3,<3.1' 'Cython'
pkgs/development/python-modules/habluetooth/default.nix-  '';
pkgs/development/python-modules/habluetooth/default.nix-
pkgs/development/python-modules/habluetooth/default.nix-  build-system = [
pkgs/development/python-modules/habluetooth/default.nix-    cython
pkgs/development/python-modules/habluetooth/default.nix-    poetry-core
pkgs/development/python-modules/habluetooth/default.nix-    setuptools
pkgs/development/python-modules/habluetooth/default.nix-  ];
pkgs/development/python-modules/habluetooth/default.nix-
pkgs/development/python-modules/habluetooth/default.nix-  dependencies = [
--
--
pkgs/development/python-modules/zope-copy/default.nix-
pkgs/development/python-modules/zope-copy/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/zope-copy/default.nix-    owner = "zopefoundation";
pkgs/development/python-modules/zope-copy/default.nix-    repo = "zope.copy";
pkgs/development/python-modules/zope-copy/default.nix-    tag = version;
pkgs/development/python-modules/zope-copy/default.nix-    hash = "sha256-uQUvfZGrMvtClXa8tLKZFYehbcBIRx7WQnumUrdQjIk=";
pkgs/development/python-modules/zope-copy/default.nix-  };
pkgs/development/python-modules/zope-copy/default.nix-
pkgs/development/python-modules/zope-copy/default.nix-  postPatch = ''
pkgs/development/python-modules/zope-copy/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/zope-copy/default.nix-      --replace-fail "setuptools < 74" "setuptools"
pkgs/development/python-modules/zope-copy/default.nix-  '';
pkgs/development/python-modules/zope-copy/default.nix-
pkgs/development/python-modules/zope-copy/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/zope-copy/default.nix-
pkgs/development/python-modules/zope-copy/default.nix-  dependencies = [
pkgs/development/python-modules/zope-copy/default.nix-    zodbpickle
pkgs/development/python-modules/zope-copy/default.nix-    zope-interface
pkgs/development/python-modules/zope-copy/default.nix-  ];
pkgs/development/python-modules/zope-copy/default.nix-
--
--
pkgs/development/python-modules/sfepy/default.nix-
pkgs/development/python-modules/sfepy/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/sfepy/default.nix-    owner = "sfepy";
pkgs/development/python-modules/sfepy/default.nix-    repo = "sfepy";
pkgs/development/python-modules/sfepy/default.nix-    tag = "release_${version}";
pkgs/development/python-modules/sfepy/default.nix-    hash = "sha256-3XQqPoAM1Qw/fZ649Xk+ceaeBkZ3ypI1FSRxtYbIrxw=";
pkgs/development/python-modules/sfepy/default.nix-  };
pkgs/development/python-modules/sfepy/default.nix-
pkgs/development/python-modules/sfepy/default.nix-  postPatch = ''
pkgs/development/python-modules/sfepy/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/sfepy/default.nix-      --replace-fail "ninja<=1.11.1.1" "ninja" \
pkgs/development/python-modules/sfepy/default.nix-      --replace-fail "numpy<2" "numpy"
pkgs/development/python-modules/sfepy/default.nix-
pkgs/development/python-modules/sfepy/default.nix:    substituteInPlace sfepy/solvers/optimize.py \
pkgs/development/python-modules/sfepy/default.nix-      --replace-fail "nm.Inf" "nm.inf"
pkgs/development/python-modules/sfepy/default.nix-
pkgs/development/python-modules/sfepy/default.nix:    substituteInPlace sfepy/examples/quantum/quantum_common.py \
pkgs/development/python-modules/sfepy/default.nix-      --replace-fail "NaN" "nan"
pkgs/development/python-modules/sfepy/default.nix-
pkgs/development/python-modules/sfepy/default.nix-    # slow tests
pkgs/development/python-modules/sfepy/default.nix-    rm sfepy/tests/test_elasticity_small_strain.py
pkgs/development/python-modules/sfepy/default.nix-    rm sfepy/tests/test_hyperelastic_tlul.py
--
pkgs/development/python-modules/jupyter-docprovider/default.nix-  pyproject = true;
pkgs/development/python-modules/jupyter-docprovider/default.nix-
pkgs/development/python-modules/jupyter-docprovider/default.nix-  src = fetchPypi {
pkgs/development/python-modules/jupyter-docprovider/default.nix-    pname = "jupyter_docprovider";
pkgs/development/python-modules/jupyter-docprovider/default.nix-    inherit version;
pkgs/development/python-modules/jupyter-docprovider/default.nix-    hash = "sha256-ivZhxlMAM0V3+i4mpltghvv2Z01ilt3rv6/XTUGMlNM=";
pkgs/development/python-modules/jupyter-docprovider/default.nix-  };
pkgs/development/python-modules/jupyter-docprovider/default.nix-
pkgs/development/python-modules/jupyter-docprovider/default.nix-  postPatch = ''
pkgs/development/python-modules/jupyter-docprovider/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/jupyter-docprovider/default.nix-      --replace-fail ', "jupyterlab>=4.0.0"' ""
pkgs/development/python-modules/jupyter-docprovider/default.nix-  '';
pkgs/development/python-modules/jupyter-docprovider/default.nix-
pkgs/development/python-modules/jupyter-docprovider/default.nix-  build-system = [
pkgs/development/python-modules/jupyter-docprovider/default.nix-    hatchling
pkgs/development/python-modules/jupyter-docprovider/default.nix-    hatch-jupyter-builder
pkgs/development/python-modules/jupyter-docprovider/default.nix-  ];
pkgs/development/python-modules/jupyter-docprovider/default.nix-
pkgs/development/python-modules/jupyter-docprovider/default.nix-  pythonImportsCheck = [ "jupyter_docprovider" ];
pkgs/development/python-modules/jupyter-docprovider/default.nix-
--
--
pkgs/development/python-modules/pescea/default.nix-    pytestCheckHook
pkgs/development/python-modules/pescea/default.nix-  ];
pkgs/development/python-modules/pescea/default.nix-
pkgs/development/python-modules/pescea/default.nix-  postPatch = ''
pkgs/development/python-modules/pescea/default.nix-    # https://github.com/lazdavila/pescea/pull/1
pkgs/development/python-modules/pescea/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/pescea/default.nix-      --replace '"asyncio",' ""
pkgs/development/python-modules/pescea/default.nix-  '';
pkgs/development/python-modules/pescea/default.nix-
pkgs/development/python-modules/pescea/default.nix-  disabledTests = [
pkgs/development/python-modules/pescea/default.nix-    # AssertionError: assert <State.BUSY: 'BusyWaiting'>...
pkgs/development/python-modules/pescea/default.nix-    "test_updates_while_busy"
pkgs/development/python-modules/pescea/default.nix-    # Test requires network access
pkgs/development/python-modules/pescea/default.nix-    "test_flow_control"
pkgs/development/python-modules/pescea/default.nix-  ];
pkgs/development/python-modules/pescea/default.nix-
--
pkgs/development/python-modules/gpu-rir/default.nix-
pkgs/development/python-modules/gpu-rir/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/gpu-rir/default.nix-    owner = "DavidDiazGuerra";
pkgs/development/python-modules/gpu-rir/default.nix-    repo = "gpuRIR";
--
pkgs/development/python-modules/pytest-golden/default.nix-
pkgs/development/python-modules/pytest-golden/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/pytest-golden/default.nix-    owner = "oprypin";
pkgs/development/python-modules/pytest-golden/default.nix-    repo = "pytest-golden";
pkgs/development/python-modules/pytest-golden/default.nix-    tag = "v${version}";
pkgs/development/python-modules/pytest-golden/default.nix-    hash = "sha256-l5fXWDK6gWJc3dkYFTokI9tWvawMRnF0td/lSwqkYXE=";
pkgs/development/python-modules/pytest-golden/default.nix-  };
pkgs/development/python-modules/pytest-golden/default.nix-
pkgs/development/python-modules/pytest-golden/default.nix-  postPatch = ''
pkgs/development/python-modules/pytest-golden/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/pytest-golden/default.nix-      --replace-fail "poetry>=0.12" poetry-core \
pkgs/development/python-modules/pytest-golden/default.nix-      --replace-fail poetry.masonry.api poetry.core.masonry.api
pkgs/development/python-modules/pytest-golden/default.nix-  '';
pkgs/development/python-modules/pytest-golden/default.nix-
pkgs/development/python-modules/pytest-golden/default.nix-  pythonRelaxDeps = [ "testfixtures" ];
pkgs/development/python-modules/pytest-golden/default.nix-
pkgs/development/python-modules/pytest-golden/default.nix-  build-system = [
pkgs/development/python-modules/pytest-golden/default.nix-    # hatchling used for > 0.2.2
pkgs/development/python-modules/pytest-golden/default.nix-    poetry-core
pkgs/development/python-modules/pytest-golden/default.nix-  ];
--
pkgs/development/python-modules/pysiaalarm/default.nix-  pyproject = true;
pkgs/development/python-modules/pysiaalarm/default.nix-
pkgs/development/python-modules/pysiaalarm/default.nix-  disabled = pythonOlder "3.8";
pkgs/development/python-modules/pysiaalarm/default.nix-
pkgs/development/python-modules/pysiaalarm/default.nix-  src = fetchPypi {
pkgs/development/python-modules/pysiaalarm/default.nix-    inherit pname version;
pkgs/development/python-modules/pysiaalarm/default.nix-    hash = "sha256-q42bsBeAwU9lt7wtYGFJv23UBND+aMXZJlSWyTfZDQE=";
pkgs/development/python-modules/pysiaalarm/default.nix-  };
pkgs/development/python-modules/pysiaalarm/default.nix-
pkgs/development/python-modules/pysiaalarm/default.nix-  postPatch = ''
pkgs/development/python-modules/pysiaalarm/default.nix:    substituteInPlace setup.cfg \
pkgs/development/python-modules/pysiaalarm/default.nix-      --replace "==" ">="
pkgs/development/python-modules/pysiaalarm/default.nix-  '';
pkgs/development/python-modules/pysiaalarm/default.nix-
pkgs/development/python-modules/pysiaalarm/default.nix-  build-system = [ setuptools-scm ];
pkgs/development/python-modules/pysiaalarm/default.nix-
pkgs/development/python-modules/pysiaalarm/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/pysiaalarm/default.nix-    dataclasses-json
pkgs/development/python-modules/pysiaalarm/default.nix-    pycryptodome
pkgs/development/python-modules/pysiaalarm/default.nix-    pytz
pkgs/development/python-modules/pysiaalarm/default.nix-  ];
--
--
pkgs/development/python-modules/zope-hookable/default.nix-
pkgs/development/python-modules/zope-hookable/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/zope-hookable/default.nix-    owner = "zopefoundation";
pkgs/development/python-modules/zope-hookable/default.nix-    repo = "zope.hookable";
pkgs/development/python-modules/zope-hookable/default.nix-    tag = version;
pkgs/development/python-modules/zope-hookable/default.nix-    hash = "sha256-qJJc646VSdNKors6Au4UAGvm7seFbvjEfpdqf//vJNE=";
pkgs/development/python-modules/zope-hookable/default.nix-  };
pkgs/development/python-modules/zope-hookable/default.nix-
pkgs/development/python-modules/zope-hookable/default.nix-  postPatch = ''
pkgs/development/python-modules/zope-hookable/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/zope-hookable/default.nix-      --replace-fail "setuptools<74" "setuptools"
pkgs/development/python-modules/zope-hookable/default.nix-  '';
pkgs/development/python-modules/zope-hookable/default.nix-
pkgs/development/python-modules/zope-hookable/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/zope-hookable/default.nix-
pkgs/development/python-modules/zope-hookable/default.nix-  pythonImportsCheck = [ "zope.hookable" ];
pkgs/development/python-modules/zope-hookable/default.nix-
pkgs/development/python-modules/zope-hookable/default.nix-  nativeCheckInputs = [ unittestCheckHook ];
pkgs/development/python-modules/zope-hookable/default.nix-
pkgs/development/python-modules/zope-hookable/default.nix-  unittestFlagsArray = [ "src/zope/hookable/tests" ];
--
--
pkgs/development/python-modules/spsdk/default.nix-
pkgs/development/python-modules/spsdk/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/spsdk/default.nix-    owner = "nxp-mcuxpresso";
pkgs/development/python-modules/spsdk/default.nix-    repo = "spsdk";
pkgs/development/python-modules/spsdk/default.nix-    tag = "v${version}";
pkgs/development/python-modules/spsdk/default.nix-    hash = "sha256-G8UNT9lsUt6Xe++xx+Pqv4hmrkGv68w7FrZSgWJHb1k=";
pkgs/development/python-modules/spsdk/default.nix-  };
pkgs/development/python-modules/spsdk/default.nix-
pkgs/development/python-modules/spsdk/default.nix-  postPatch = ''
pkgs/development/python-modules/spsdk/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/spsdk/default.nix-      --replace-fail "setuptools>=72.1,<74" "setuptools" \
pkgs/development/python-modules/spsdk/default.nix-      --replace-fail "setuptools_scm<8.2" "setuptools_scm"
pkgs/development/python-modules/spsdk/default.nix-  '';
pkgs/development/python-modules/spsdk/default.nix-
pkgs/development/python-modules/spsdk/default.nix-  build-system = [
pkgs/development/python-modules/spsdk/default.nix-    setuptools
pkgs/development/python-modules/spsdk/default.nix-    setuptools-scm
pkgs/development/python-modules/spsdk/default.nix-  ];
pkgs/development/python-modules/spsdk/default.nix-
pkgs/development/python-modules/spsdk/default.nix-  pythonRelaxDeps = [
--
pkgs/development/python-modules/notebook/default.nix-  pyproject = true;
--
pkgs/development/python-modules/bwapy/default.nix-  src = fetchPypi {
pkgs/development/python-modules/bwapy/default.nix-    inherit pname version;
pkgs/development/python-modules/bwapy/default.nix-    sha256 = "090qwx3vl729zn3a7sksbviyg04kc71gpbm3nd8dalqp673x1npw";
pkgs/development/python-modules/bwapy/default.nix-  };
pkgs/development/python-modules/bwapy/default.nix-  postPatch = ''
pkgs/development/python-modules/bwapy/default.nix-    # replace bundled bwa
pkgs/development/python-modules/bwapy/default.nix-    rm -r bwa/*
pkgs/development/python-modules/bwapy/default.nix-    cp ${bwa}/lib/*.a ${bwa}/include/*.h bwa/
pkgs/development/python-modules/bwapy/default.nix-
pkgs/development/python-modules/bwapy/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/bwapy/default.nix-      --replace 'setuptools>=49.2.0' 'setuptools'
pkgs/development/python-modules/bwapy/default.nix-  '';
pkgs/development/python-modules/bwapy/default.nix-
pkgs/development/python-modules/bwapy/default.nix-  buildInputs = [
pkgs/development/python-modules/bwapy/default.nix-    zlib
pkgs/development/python-modules/bwapy/default.nix-    bwa
pkgs/development/python-modules/bwapy/default.nix-  ];
pkgs/development/python-modules/bwapy/default.nix-
pkgs/development/python-modules/bwapy/default.nix-  propagatedBuildInputs = [ cffi ];
pkgs/development/python-modules/bwapy/default.nix-
--
--
pkgs/development/python-modules/bubop/default.nix-    pyyaml
--
pkgs/development/python-modules/pyzstd/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/pyzstd/default.nix-    owner = "Rogdham";
pkgs/development/python-modules/pyzstd/default.nix-    repo = "pyzstd";
pkgs/development/python-modules/pyzstd/default.nix-    tag = version;
pkgs/development/python-modules/pyzstd/default.nix-    hash = "sha256-PICYdB/xu/q2wjbkF2nziZt8z8PmzJ5eM+Yq0rpLfEU=";
pkgs/development/python-modules/pyzstd/default.nix-  };
pkgs/development/python-modules/pyzstd/default.nix-
pkgs/development/python-modules/pyzstd/default.nix-  postPatch = ''
pkgs/development/python-modules/pyzstd/default.nix-    # pyzst specifies setuptools<74 because 74+ drops `distutils.msvc9compiler`,
pkgs/development/python-modules/pyzstd/default.nix-    # required for Python 3.9 under Windows
pkgs/development/python-modules/pyzstd/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/pyzstd/default.nix-        --replace-fail '"setuptools>=64,<74"' '"setuptools"'
pkgs/development/python-modules/pyzstd/default.nix-  '';
pkgs/development/python-modules/pyzstd/default.nix-
pkgs/development/python-modules/pyzstd/default.nix-  nativeBuildInputs = [
pkgs/development/python-modules/pyzstd/default.nix-    setuptools
pkgs/development/python-modules/pyzstd/default.nix-  ];
pkgs/development/python-modules/pyzstd/default.nix-
pkgs/development/python-modules/pyzstd/default.nix-  build-system = [
pkgs/development/python-modules/pyzstd/default.nix-    setuptools
pkgs/development/python-modules/pyzstd/default.nix-  ];
--
--
pkgs/development/python-modules/zha/default.nix-
pkgs/development/python-modules/zha/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/zha/default.nix-    owner = "zigpy";
pkgs/development/python-modules/zha/default.nix-    repo = "zha";
pkgs/development/python-modules/zha/default.nix-    tag = version;
pkgs/development/python-modules/zha/default.nix-    hash = "sha256-NgUUzNfC1XngU5RBfbKpt/o8hu7XRXOUaDUb7OjSJJc=";
pkgs/development/python-modules/zha/default.nix-  };
pkgs/development/python-modules/zha/default.nix-
pkgs/development/python-modules/zha/default.nix-  postPatch = ''
pkgs/development/python-modules/zha/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/zha/default.nix-      --replace-fail '"setuptools-git-versioning<3"' "" \
pkgs/development/python-modules/zha/default.nix-      --replace-fail 'dynamic = ["version"]' 'version = "${version}"'
pkgs/development/python-modules/zha/default.nix-  '';
pkgs/development/python-modules/zha/default.nix-
pkgs/development/python-modules/zha/default.nix-  build-system = [
pkgs/development/python-modules/zha/default.nix-    setuptools
pkgs/development/python-modules/zha/default.nix-    wheel
pkgs/development/python-modules/zha/default.nix-  ];
pkgs/development/python-modules/zha/default.nix-
pkgs/development/python-modules/zha/default.nix-  dependencies = [
--
--
pkgs/development/python-modules/anthropic/default.nix-
pkgs/development/python-modules/anthropic/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/anthropic/default.nix-    owner = "anthropics";
pkgs/development/python-modules/anthropic/default.nix-    repo = "anthropic-sdk-python";
pkgs/development/python-modules/anthropic/default.nix-    tag = "v${version}";
pkgs/development/python-modules/anthropic/default.nix-    hash = "sha256-EVLSC6ClHnmGqMoefMXj3M4dh812ZN5t9nF3gfCLyCo=";
pkgs/development/python-modules/anthropic/default.nix-  };
pkgs/development/python-modules/anthropic/default.nix-
pkgs/development/python-modules/anthropic/default.nix-  postPatch = ''
pkgs/development/python-modules/anthropic/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/anthropic/default.nix-      --replace-fail '"hatchling==1.26.3"' '"hatchling>=1.26.3"'
pkgs/development/python-modules/anthropic/default.nix-  '';
pkgs/development/python-modules/anthropic/default.nix-
pkgs/development/python-modules/anthropic/default.nix-  build-system = [
pkgs/development/python-modules/anthropic/default.nix-    hatchling
pkgs/development/python-modules/anthropic/default.nix-    hatch-fancy-pypi-readme
pkgs/development/python-modules/anthropic/default.nix-  ];
pkgs/development/python-modules/anthropic/default.nix-
pkgs/development/python-modules/anthropic/default.nix-  dependencies = [
pkgs/development/python-modules/anthropic/default.nix-    anyio
--
pkgs/development/python-modules/scapy/default.nix-  patches = [ ./find-library.patch ];
pkgs/development/python-modules/scapy/default.nix-
pkgs/development/python-modules/scapy/default.nix-  postPatch = ''
pkgs/development/python-modules/scapy/default.nix-    printf "${version}" > scapy/VERSION
pkgs/development/python-modules/scapy/default.nix-
pkgs/development/python-modules/scapy/default.nix-    libpcap_file="${lib.getLib libpcap}/lib/libpcap${stdenv.hostPlatform.extensions.sharedLibrary}"
pkgs/development/python-modules/scapy/default.nix-    if ! [ -e "$libpcap_file" ]; then
pkgs/development/python-modules/scapy/default.nix-        echo "error: $libpcap_file not found" >&2
pkgs/development/python-modules/scapy/default.nix-        exit 1
pkgs/development/python-modules/scapy/default.nix-    fi
pkgs/development/python-modules/scapy/default.nix:    substituteInPlace "scapy/libs/winpcapy.py" \
pkgs/development/python-modules/scapy/default.nix-        --replace "@libpcap_file@" "$libpcap_file"
pkgs/development/python-modules/scapy/default.nix-  ''
pkgs/development/python-modules/scapy/default.nix-  + lib.optionalString withManufDb ''
pkgs/development/python-modules/scapy/default.nix:    substituteInPlace scapy/data.py --replace "/opt/wireshark" "${wireshark}"
pkgs/development/python-modules/scapy/default.nix-  '';
pkgs/development/python-modules/scapy/default.nix-
pkgs/development/python-modules/scapy/default.nix-  buildInputs = lib.optional withVoipSupport sox;
--
pkgs/development/python-modules/zigpy-xbee/default.nix-
pkgs/development/python-modules/zigpy-xbee/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/zigpy-xbee/default.nix-    owner = "zigpy";
pkgs/development/python-modules/zigpy-xbee/default.nix-    repo = "zigpy-xbee";
pkgs/development/python-modules/zigpy-xbee/default.nix-    tag = version;
pkgs/development/python-modules/zigpy-xbee/default.nix-    hash = "sha256-Ep7pP2vcH9YpSrGPVDi3nc+WkQgBVS+NLmoQU0o0aQQ=";
pkgs/development/python-modules/zigpy-xbee/default.nix-  };
pkgs/development/python-modules/zigpy-xbee/default.nix-
pkgs/development/python-modules/zigpy-xbee/default.nix-  postPatch = ''
pkgs/development/python-modules/zigpy-xbee/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/zigpy-xbee/default.nix-      --replace ', "setuptools-git-versioning<2"' "" \
pkgs/development/python-modules/zigpy-xbee/default.nix-      --replace 'dynamic = ["version"]' 'version = "${version}"'
pkgs/development/python-modules/zigpy-xbee/default.nix-  '';
pkgs/development/python-modules/zigpy-xbee/default.nix-
pkgs/development/python-modules/zigpy-xbee/default.nix-  nativeBuildInputs = [ setuptools ];
pkgs/development/python-modules/zigpy-xbee/default.nix-
pkgs/development/python-modules/zigpy-xbee/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/zigpy-xbee/default.nix-    pyserial
pkgs/development/python-modules/zigpy-xbee/default.nix-    pyserial-asyncio
pkgs/development/python-modules/zigpy-xbee/default.nix-    zigpy
--
--
pkgs/development/python-modules/pylibjpeg-openjpeg/default.nix-    hash = "sha256-siZ/Mm1wmd7dWhGa4rdH9Frxis2jB9av/Kw2dEe5dpI=";
pkgs/development/python-modules/pylibjpeg-openjpeg/default.nix-  };
pkgs/development/python-modules/pylibjpeg-openjpeg/default.nix-
pkgs/development/python-modules/pylibjpeg-openjpeg/default.nix-  # don't use vendored openjpeg submodule:
pkgs/development/python-modules/pylibjpeg-openjpeg/default.nix-  # (note build writes into openjpeg source dir, so we have to make it writable)
pkgs/development/python-modules/pylibjpeg-openjpeg/default.nix-  postPatch = ''
pkgs/development/python-modules/pylibjpeg-openjpeg/default.nix-    rmdir lib/openjpeg
pkgs/development/python-modules/pylibjpeg-openjpeg/default.nix-    cp -r ${openjpeg.src} lib/openjpeg
pkgs/development/python-modules/pylibjpeg-openjpeg/default.nix-    chmod +rwX -R lib/openjpeg
pkgs/development/python-modules/pylibjpeg-openjpeg/default.nix-
pkgs/development/python-modules/pylibjpeg-openjpeg/default.nix:    substituteInPlace pyproject.toml --replace-fail "poetry-core >=1.8,<2" "poetry-core"
pkgs/development/python-modules/pylibjpeg-openjpeg/default.nix-  '';
pkgs/development/python-modules/pylibjpeg-openjpeg/default.nix-
pkgs/development/python-modules/pylibjpeg-openjpeg/default.nix-  dontUseCmakeConfigure = true;
pkgs/development/python-modules/pylibjpeg-openjpeg/default.nix-
pkgs/development/python-modules/pylibjpeg-openjpeg/default.nix-  build-system = [
pkgs/development/python-modules/pylibjpeg-openjpeg/default.nix-    cmake
pkgs/development/python-modules/pylibjpeg-openjpeg/default.nix-    cython
pkgs/development/python-modules/pylibjpeg-openjpeg/default.nix-    poetry-core
pkgs/development/python-modules/pylibjpeg-openjpeg/default.nix-    setuptools
pkgs/development/python-modules/pylibjpeg-openjpeg/default.nix-  ];
--
pkgs/development/python-modules/dbus-deviation/default.nix-  version = "0.6.1";
pkgs/development/python-modules/dbus-deviation/default.nix-  pyproject = true;
pkgs/development/python-modules/dbus-deviation/default.nix-
pkgs/development/python-modules/dbus-deviation/default.nix-  src = fetchPypi {
pkgs/development/python-modules/dbus-deviation/default.nix-    inherit pname version;
pkgs/development/python-modules/dbus-deviation/default.nix-    hash = "sha256-4GuI7+IjiF0nJd9Rz3ybe0Y9HG8E6knUaQh0MY0Ot6M=";
pkgs/development/python-modules/dbus-deviation/default.nix-  };
pkgs/development/python-modules/dbus-deviation/default.nix-
pkgs/development/python-modules/dbus-deviation/default.nix-  postPatch = ''
pkgs/development/python-modules/dbus-deviation/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/dbus-deviation/default.nix-      --replace-fail "'setuptools_git >= 0.3'," "" \
pkgs/development/python-modules/dbus-deviation/default.nix-      --replace-fail "'sphinx'," ""
pkgs/development/python-modules/dbus-deviation/default.nix-  '';
pkgs/development/python-modules/dbus-deviation/default.nix-
pkgs/development/python-modules/dbus-deviation/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/dbus-deviation/default.nix-  dependencies = [ lxml ];
pkgs/development/python-modules/dbus-deviation/default.nix-
pkgs/development/python-modules/dbus-deviation/default.nix-  pythonImportsCheck = [ "dbusdeviation" ];
pkgs/development/python-modules/dbus-deviation/default.nix-
pkgs/development/python-modules/dbus-deviation/default.nix-  meta = with lib; {
--
--
pkgs/development/python-modules/restrictedpython/default.nix-
pkgs/development/python-modules/restrictedpython/default.nix-  disabled = pythonOlder "3.7";
pkgs/development/python-modules/restrictedpython/default.nix-
pkgs/development/python-modules/restrictedpython/default.nix-  src = fetchPypi {
pkgs/development/python-modules/restrictedpython/default.nix-    inherit pname version;
pkgs/development/python-modules/restrictedpython/default.nix-    hash = "sha256-OvIxK8Z+X87Yh/uFsAbImGHackiBKLFVvuqB62oKmyQ=";
pkgs/development/python-modules/restrictedpython/default.nix-  };
pkgs/development/python-modules/restrictedpython/default.nix-
pkgs/development/python-modules/restrictedpython/default.nix-  postPatch = ''
pkgs/development/python-modules/restrictedpython/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/restrictedpython/default.nix-      --replace-fail "setuptools <= 75.6.0" setuptools
pkgs/development/python-modules/restrictedpython/default.nix-  '';
pkgs/development/python-modules/restrictedpython/default.nix-
pkgs/development/python-modules/restrictedpython/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/restrictedpython/default.nix-
pkgs/development/python-modules/restrictedpython/default.nix-  nativeCheckInputs = [
pkgs/development/python-modules/restrictedpython/default.nix-    pytestCheckHook
pkgs/development/python-modules/restrictedpython/default.nix-    pytest-mock
pkgs/development/python-modules/restrictedpython/default.nix-  ];
pkgs/development/python-modules/restrictedpython/default.nix-
--
--
pkgs/development/python-modules/gerbonara/default.nix-  # Test environment is exceptionally tricky to get set up, so skip for now.
pkgs/development/python-modules/gerbonara/default.nix-  doCheck = false;
pkgs/development/python-modules/gerbonara/default.nix-
pkgs/development/python-modules/gerbonara/default.nix-  passthru.updateScript = gitUpdater { rev-prefix = "v"; };
--
pkgs/development/python-modules/qscintilla/default.nix-  dontWrapQtApps = true;
pkgs/development/python-modules/qscintilla/default.nix-
pkgs/development/python-modules/qscintilla/default.nix-  postPatch = ''
pkgs/development/python-modules/qscintilla/default.nix-    cd Python
pkgs/development/python-modules/qscintilla/default.nix-    cp pyproject-qt${qtVersion}.toml pyproject.toml
pkgs/development/python-modules/qscintilla/default.nix-    echo '[tool.sip.project]' >> pyproject.toml
pkgs/development/python-modules/qscintilla/default.nix-    echo 'sip-include-dirs = [ "${pyQtPackage}/${python.sitePackages}/PyQt${qtVersion}/bindings"]' \
pkgs/development/python-modules/qscintilla/default.nix-       >> pyproject.toml
pkgs/development/python-modules/qscintilla/default.nix-  ''
pkgs/development/python-modules/qscintilla/default.nix-  + lib.optionalString stdenv.hostPlatform.isDarwin ''
pkgs/development/python-modules/qscintilla/default.nix:    substituteInPlace project.py \
pkgs/development/python-modules/qscintilla/default.nix-      --replace \
pkgs/development/python-modules/qscintilla/default.nix-      "if self.project.qsci_external_lib:
pkgs/development/python-modules/qscintilla/default.nix-                if self.qsci_features_dir is not None:" \
pkgs/development/python-modules/qscintilla/default.nix-      "if self.project.qsci_external_lib:
pkgs/development/python-modules/qscintilla/default.nix-                self.builder_settings.append('QT += widgets')
pkgs/development/python-modules/qscintilla/default.nix-
pkgs/development/python-modules/qscintilla/default.nix-                self.builder_settings.append('QT += printsupport')
--
pkgs/development/python-modules/jsonschema-spec/default.nix-
pkgs/development/python-modules/jsonschema-spec/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/jsonschema-spec/default.nix-    owner = "p1c2u";
pkgs/development/python-modules/jsonschema-spec/default.nix-    repo = "jsonschema-spec";
pkgs/development/python-modules/jsonschema-spec/default.nix-    tag = version;
pkgs/development/python-modules/jsonschema-spec/default.nix-    hash = "sha256-rCepDnVAOEsokKjWCuqDYbGIq6/wn4rsQRx5dXTUsYo=";
pkgs/development/python-modules/jsonschema-spec/default.nix-  };
pkgs/development/python-modules/jsonschema-spec/default.nix-
pkgs/development/python-modules/jsonschema-spec/default.nix-  postPatch = ''
pkgs/development/python-modules/jsonschema-spec/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/jsonschema-spec/default.nix-      --replace 'referencing = ">=0.28.0,<0.30.0"' 'referencing = ">=0.28.0"'
pkgs/development/python-modules/jsonschema-spec/default.nix-  '';
pkgs/development/python-modules/jsonschema-spec/default.nix-
pkgs/development/python-modules/jsonschema-spec/default.nix-  nativeBuildInputs = [
pkgs/development/python-modules/jsonschema-spec/default.nix-    poetry-core
pkgs/development/python-modules/jsonschema-spec/default.nix-  ];
pkgs/development/python-modules/jsonschema-spec/default.nix-
pkgs/development/python-modules/jsonschema-spec/default.nix-  pythonRelaxDeps = [ "referencing" ];
pkgs/development/python-modules/jsonschema-spec/default.nix-
pkgs/development/python-modules/jsonschema-spec/default.nix-  propagatedBuildInputs = [
--
--
pkgs/development/python-modules/pyannote-audio/default.nix-
pkgs/development/python-modules/pyannote-audio/default.nix-  pythonRelaxDeps = [ "torchaudio" ];
pkgs/development/python-modules/pyannote-audio/default.nix-
pkgs/development/python-modules/pyannote-audio/default.nix-  build-system = [
pkgs/development/python-modules/pyannote-audio/default.nix-    pyscaffold
pkgs/development/python-modules/pyannote-audio/default.nix-    setuptools
pkgs/development/python-modules/pyannote-audio/default.nix-  ];
pkgs/development/python-modules/pyannote-audio/default.nix-
pkgs/development/python-modules/pyannote-audio/default.nix-  postPatch = ''
pkgs/development/python-modules/pyannote-audio/default.nix:    substituteInPlace setup.cfg \
pkgs/development/python-modules/pyannote-audio/default.nix-      --replace-fail "pyscaffold>=3.2a0,<3.3a0" "pyscaffold"
pkgs/development/python-modules/pyannote-audio/default.nix:    substituteInPlace requirements.txt \
pkgs/development/python-modules/pyannote-audio/default.nix-      --replace-fail "lightning" "pytorch-lightning"
pkgs/development/python-modules/pyannote-audio/default.nix-  '';
pkgs/development/python-modules/pyannote-audio/default.nix-
pkgs/development/python-modules/pyannote-audio/default.nix-  dependencies = [
pkgs/development/python-modules/pyannote-audio/default.nix-    asteroid-filterbanks
pkgs/development/python-modules/pyannote-audio/default.nix-    einops
pkgs/development/python-modules/pyannote-audio/default.nix-    huggingface-hub
pkgs/development/python-modules/pyannote-audio/default.nix-    omegaconf
pkgs/development/python-modules/pyannote-audio/default.nix-    pyannote-core
--
pkgs/development/python-modules/flask-caching/default.nix-  disabled = pythonOlder "3.7";
pkgs/development/python-modules/flask-caching/default.nix-
pkgs/development/python-modules/flask-caching/default.nix-  src = fetchPypi {
pkgs/development/python-modules/flask-caching/default.nix-    pname = "flask_caching";
pkgs/development/python-modules/flask-caching/default.nix-    inherit version;
pkgs/development/python-modules/flask-caching/default.nix-    hash = "sha256-Zdf9G07r+BD4RN595iWCVLMkgpbuQpvcs/dBvL97mMk=";
pkgs/development/python-modules/flask-caching/default.nix-  };
pkgs/development/python-modules/flask-caching/default.nix-
pkgs/development/python-modules/flask-caching/default.nix-  postPatch = ''
pkgs/development/python-modules/flask-caching/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/flask-caching/default.nix-      --replace "cachelib >= 0.9.0, < 0.10.0" "cachelib"
pkgs/development/python-modules/flask-caching/default.nix-  '';
pkgs/development/python-modules/flask-caching/default.nix-
pkgs/development/python-modules/flask-caching/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/flask-caching/default.nix-    cachelib
pkgs/development/python-modules/flask-caching/default.nix-    flask
pkgs/development/python-modules/flask-caching/default.nix-  ];
pkgs/development/python-modules/flask-caching/default.nix-
pkgs/development/python-modules/flask-caching/default.nix-  nativeCheckInputs = [
pkgs/development/python-modules/flask-caching/default.nix-    asgiref
--
--
pkgs/development/python-modules/periodiq/default.nix-
pkgs/development/python-modules/periodiq/default.nix-  src = fetchFromGitLab {
pkgs/development/python-modules/periodiq/default.nix-    owner = "bersace";
pkgs/development/python-modules/periodiq/default.nix-    repo = "periodiq";
pkgs/development/python-modules/periodiq/default.nix-    tag = "v${version}";
pkgs/development/python-modules/periodiq/default.nix-    hash = "sha256-Pyh/T3/HGPYyaXjyM0wkQ1V7p5ibqxE1Q62QwCIJ8To=";
pkgs/development/python-modules/periodiq/default.nix-  };
pkgs/development/python-modules/periodiq/default.nix-
pkgs/development/python-modules/periodiq/default.nix-  postPatch = ''
pkgs/development/python-modules/periodiq/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/periodiq/default.nix-      --replace-fail 'poetry>=0.12' 'poetry-core' \
pkgs/development/python-modules/periodiq/default.nix-      --replace-fail 'poetry.masonry.api' 'poetry.core.masonry.api'
pkgs/development/python-modules/periodiq/default.nix-  '';
pkgs/development/python-modules/periodiq/default.nix-
pkgs/development/python-modules/periodiq/default.nix-  nativeBuildInputs = [ poetry-core ];
pkgs/development/python-modules/periodiq/default.nix-
pkgs/development/python-modules/periodiq/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/periodiq/default.nix-    dramatiq
pkgs/development/python-modules/periodiq/default.nix-    pendulum
pkgs/development/python-modules/periodiq/default.nix-    setuptools
--
--
pkgs/development/python-modules/luna-soc/default.nix-
pkgs/development/python-modules/luna-soc/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/luna-soc/default.nix-    owner = "greatscottgadgets";
pkgs/development/python-modules/luna-soc/default.nix-    repo = "luna-soc";
pkgs/development/python-modules/luna-soc/default.nix-    tag = version;
pkgs/development/python-modules/luna-soc/default.nix-    hash = "sha256-Rks1wC0CR5FSu4TrE1thzolT3QBd0yh7q+SxZ1U+pB4=";
pkgs/development/python-modules/luna-soc/default.nix-  };
pkgs/development/python-modules/luna-soc/default.nix-
pkgs/development/python-modules/luna-soc/default.nix-  postPatch = ''
pkgs/development/python-modules/luna-soc/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/luna-soc/default.nix-      --replace-fail '"setuptools-git-versioning<2"' "" \
pkgs/development/python-modules/luna-soc/default.nix-      --replace-fail 'dynamic = ["version"]' 'version = "${version}"'
pkgs/development/python-modules/luna-soc/default.nix-  '';
pkgs/development/python-modules/luna-soc/default.nix-
pkgs/development/python-modules/luna-soc/default.nix-  build-system = [
pkgs/development/python-modules/luna-soc/default.nix-    setuptools
pkgs/development/python-modules/luna-soc/default.nix-  ];
pkgs/development/python-modules/luna-soc/default.nix-
pkgs/development/python-modules/luna-soc/default.nix-  dependencies = [ luna-usb ];
pkgs/development/python-modules/luna-soc/default.nix-
--
--
pkgs/development/python-modules/argostranslate/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/argostranslate/default.nix-    ctranslate2OneDNN
pkgs/development/python-modules/argostranslate/default.nix-    sentencepiece
pkgs/development/python-modules/argostranslate/default.nix-    stanza
pkgs/development/python-modules/argostranslate/default.nix-  ];
pkgs/development/python-modules/argostranslate/default.nix-
pkgs/development/python-modules/argostranslate/default.nix-  postPatch = ''
pkgs/development/python-modules/argostranslate/default.nix-    ln -s */requires.txt requirements.txt
pkgs/development/python-modules/argostranslate/default.nix-
pkgs/development/python-modules/argostranslate/default.nix:    substituteInPlace requirements.txt  \
pkgs/development/python-modules/argostranslate/default.nix-      --replace "==" ">="
pkgs/development/python-modules/argostranslate/default.nix-  '';
pkgs/development/python-modules/argostranslate/default.nix-
pkgs/development/python-modules/argostranslate/default.nix-  doCheck = false; # needs network access
pkgs/development/python-modules/argostranslate/default.nix-
pkgs/development/python-modules/argostranslate/default.nix-  nativeCheckInputs = [ pytestCheckHook ];
pkgs/development/python-modules/argostranslate/default.nix-
pkgs/development/python-modules/argostranslate/default.nix-  # required for import check to work
pkgs/development/python-modules/argostranslate/default.nix-  # PermissionError: [Errno 13] Permission denied: '/homeless-shelter'
pkgs/development/python-modules/argostranslate/default.nix-  env.HOME = "/tmp";
--
--
--
pkgs/development/python-modules/okonomiyaki/default.nix-
pkgs/development/python-modules/okonomiyaki/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/okonomiyaki/default.nix-    owner = "enthought";
pkgs/development/python-modules/okonomiyaki/default.nix-    repo = "okonomiyaki";
pkgs/development/python-modules/okonomiyaki/default.nix-    tag = version;
pkgs/development/python-modules/okonomiyaki/default.nix-    hash = "sha256-xAF9Tdr+IM3lU+mcNcAWATJLZOVvbx0llqznqHLVqDc=";
pkgs/development/python-modules/okonomiyaki/default.nix-  };
pkgs/development/python-modules/okonomiyaki/default.nix-
pkgs/development/python-modules/okonomiyaki/default.nix-  postPatch = ''
pkgs/development/python-modules/okonomiyaki/default.nix-    # Fixed for >= 2.0.0
pkgs/development/python-modules/okonomiyaki/default.nix:    substituteInPlace setup.cfg \
pkgs/development/python-modules/okonomiyaki/default.nix-      --replace-fail "long_description_content_type = rst" "long_description_content_type = text/x-rst"
pkgs/development/python-modules/okonomiyaki/default.nix-  '';
pkgs/development/python-modules/okonomiyaki/default.nix-
pkgs/development/python-modules/okonomiyaki/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/okonomiyaki/default.nix-
pkgs/development/python-modules/okonomiyaki/default.nix-  optional-dependencies = {
pkgs/development/python-modules/okonomiyaki/default.nix-    all = [
pkgs/development/python-modules/okonomiyaki/default.nix-      attrs
pkgs/development/python-modules/okonomiyaki/default.nix-      distro
--
pkgs/development/python-modules/symengine/default.nix-    tag = "v${version}";
pkgs/development/python-modules/symengine/default.nix-    hash = "sha256-adzODm7gAqwAf7qzfRQ1AG8mC3auiXM4OsV/0h+ZmUg=";
pkgs/development/python-modules/symengine/default.nix-  };
pkgs/development/python-modules/symengine/default.nix-
pkgs/development/python-modules/symengine/default.nix-  env = {
pkgs/development/python-modules/symengine/default.nix-    SymEngine_DIR = "${symengine}";
pkgs/development/python-modules/symengine/default.nix-  };
pkgs/development/python-modules/symengine/default.nix-
pkgs/development/python-modules/symengine/default.nix-  postPatch = ''
pkgs/development/python-modules/symengine/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/symengine/default.nix-      --replace-fail "'cython>=0.29.24'" "'cython'"
pkgs/development/python-modules/symengine/default.nix-  '';
pkgs/development/python-modules/symengine/default.nix-
pkgs/development/python-modules/symengine/default.nix-  dontUseCmakeConfigure = true;
pkgs/development/python-modules/symengine/default.nix-  nativeBuildInputs = [
pkgs/development/python-modules/symengine/default.nix-    cmake
pkgs/development/python-modules/symengine/default.nix-    cython
pkgs/development/python-modules/symengine/default.nix-  ];
pkgs/development/python-modules/symengine/default.nix-
pkgs/development/python-modules/symengine/default.nix-  nativeCheckInputs = [
--
--
pkgs/development/python-modules/napari/default.nix-
pkgs/development/python-modules/napari/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/napari/default.nix-    owner = "napari";
pkgs/development/python-modules/napari/default.nix-    repo = "napari";
pkgs/development/python-modules/napari/default.nix-    tag = "v${version}";
pkgs/development/python-modules/napari/default.nix-    hash = "sha256-OPbjq9jXA5onLBCVvCx4g935y7GNvf4GA5s5sfNjIKY=";
pkgs/development/python-modules/napari/default.nix-  };
pkgs/development/python-modules/napari/default.nix-
pkgs/development/python-modules/napari/default.nix-  postPatch = ''
pkgs/development/python-modules/napari/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/napari/default.nix-      --replace-fail "scikit-image[data]>=0.19.1" "scikit-image"
pkgs/development/python-modules/napari/default.nix-  '';
pkgs/development/python-modules/napari/default.nix-
pkgs/development/python-modules/napari/default.nix-  build-system = [
pkgs/development/python-modules/napari/default.nix-    setuptools
pkgs/development/python-modules/napari/default.nix-    setuptools-scm
pkgs/development/python-modules/napari/default.nix-  ];
pkgs/development/python-modules/napari/default.nix-
pkgs/development/python-modules/napari/default.nix-  nativeBuildInputs = [ wrapQtAppsHook ];
pkgs/development/python-modules/napari/default.nix-
--
--
pkgs/development/python-modules/spyse-python/default.nix-      name = "support-later-limiter.patch";
pkgs/development/python-modules/spyse-python/default.nix-      url = "https://github.com/spyse-com/spyse-python/commit/ff68164c514dfb28ab77d8690b3a5153962dbe8c.patch";
pkgs/development/python-modules/spyse-python/default.nix-      hash = "sha256-PoWPJCK/Scsh4P7lr97u4JpVHXNlY0C9rJgY4TDYmv0=";
pkgs/development/python-modules/spyse-python/default.nix-    })
pkgs/development/python-modules/spyse-python/default.nix-  ];
pkgs/development/python-modules/spyse-python/default.nix-
pkgs/development/python-modules/spyse-python/default.nix-  pythonRemoveDeps = [ "dataclasses" ];
pkgs/development/python-modules/spyse-python/default.nix-
pkgs/development/python-modules/spyse-python/default.nix-  postPatch = ''
pkgs/development/python-modules/spyse-python/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/spyse-python/default.nix-      --replace-fail "dataclasses-json~=0.5.4" "dataclasses-json>=0.5.4" \
pkgs/development/python-modules/spyse-python/default.nix-      --replace-fail "responses~=0.13.3" "responses>=0.13.3" \
pkgs/development/python-modules/spyse-python/default.nix-      --replace-fail "limiter~=0.1.2" "limiter>=0.1.2" \
pkgs/development/python-modules/spyse-python/default.nix-      --replace-fail "requests~=2.26.0" "requests>=2.26.0"
pkgs/development/python-modules/spyse-python/default.nix-  '';
pkgs/development/python-modules/spyse-python/default.nix-
pkgs/development/python-modules/spyse-python/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/spyse-python/default.nix-
pkgs/development/python-modules/spyse-python/default.nix-  dependencies = [
pkgs/development/python-modules/spyse-python/default.nix-    requests
--
pkgs/development/python-modules/twisted/default.nix-      };
pkgs/development/python-modules/twisted/default.nix-    in
pkgs/development/python-modules/twisted/default.nix-    lib.concatStringsSep "\n" (
pkgs/development/python-modules/twisted/default.nix-      lib.mapAttrsToList (
pkgs/development/python-modules/twisted/default.nix-        file: tests: lib.concatMapStringsSep "\n" (test: ''echo '${test}.skip = ""' >> "${file}"'') tests
pkgs/development/python-modules/twisted/default.nix-      ) skippedTests
pkgs/development/python-modules/twisted/default.nix-    )
pkgs/development/python-modules/twisted/default.nix-    + lib.optionalString stdenv.hostPlatform.isLinux ''
pkgs/development/python-modules/twisted/default.nix-      # Patch t.p._inotify to point to libc. Without this,
pkgs/development/python-modules/twisted/default.nix-      # twisted.python.runtime.platform.supportsINotify() == False
pkgs/development/python-modules/twisted/default.nix:      substituteInPlace src/twisted/python/_inotify.py --replace-fail \
pkgs/development/python-modules/twisted/default.nix-        "ctypes.util.find_library(\"c\")" "'${stdenv.cc.libc}/lib/libc.so.6'"
pkgs/development/python-modules/twisted/default.nix-    '';
pkgs/development/python-modules/twisted/default.nix-
pkgs/development/python-modules/twisted/default.nix-  # Generate Twisted's plug-in cache. Twisted users must do it as well. See
pkgs/development/python-modules/twisted/default.nix-  # http://twistedmatrix.com/documents/current/core/howto/plugin.html#auto3
pkgs/development/python-modules/twisted/default.nix-  # and http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=477103 for details.
pkgs/development/python-modules/twisted/default.nix-  postFixup = lib.optionalString (stdenv.buildPlatform.canExecute stdenv.hostPlatform) ''
pkgs/development/python-modules/twisted/default.nix-    $out/bin/twistd --help > /dev/null
pkgs/development/python-modules/twisted/default.nix-  '';
pkgs/development/python-modules/twisted/default.nix-
--
pkgs/development/python-modules/pyaftership/default.nix-
pkgs/development/python-modules/pyaftership/default.nix-  nativeCheckInputs = [
pkgs/development/python-modules/pyaftership/default.nix-    aresponses
pkgs/development/python-modules/pyaftership/default.nix-    pytest-asyncio
pkgs/development/python-modules/pyaftership/default.nix-    pytestCheckHook
pkgs/development/python-modules/pyaftership/default.nix-  ];
pkgs/development/python-modules/pyaftership/default.nix-
--
pkgs/development/python-modules/commentjson/default.nix-
pkgs/development/python-modules/commentjson/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/commentjson/default.nix-    owner = "vaidik";
pkgs/development/python-modules/commentjson/default.nix-    repo = "commentjson";
pkgs/development/python-modules/commentjson/default.nix-    rev = "v${version}";
pkgs/development/python-modules/commentjson/default.nix-    hash = "sha256-dPnIcv7TIeyG7rU938w7FrDklmaGuPpXz34uw/JjOgY=";
pkgs/development/python-modules/commentjson/default.nix-  };
pkgs/development/python-modules/commentjson/default.nix-
pkgs/development/python-modules/commentjson/default.nix-  postPatch = ''
pkgs/development/python-modules/commentjson/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/commentjson/default.nix-      --replace "lark-parser>=0.7.1,<0.8.0" "lark"
pkgs/development/python-modules/commentjson/default.nix-
pkgs/development/python-modules/commentjson/default.nix-    # NixOS is missing test.test_json module
pkgs/development/python-modules/commentjson/default.nix-    rm -r commentjson/tests/test_json
pkgs/development/python-modules/commentjson/default.nix-  '';
pkgs/development/python-modules/commentjson/default.nix-
pkgs/development/python-modules/commentjson/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/commentjson/default.nix-    lark
pkgs/development/python-modules/commentjson/default.nix-    six
pkgs/development/python-modules/commentjson/default.nix-  ];
--
--
pkgs/development/python-modules/matplotlib/default.nix-  env.XDG_RUNTIME_DIR = "/tmp";
pkgs/development/python-modules/matplotlib/default.nix-
pkgs/development/python-modules/matplotlib/default.nix-  # Matplotlib tries to find Tcl/Tk by opening a Tk window and asking the
pkgs/development/python-modules/matplotlib/default.nix-  # corresponding interpreter object for its library paths. This fails if
pkgs/development/python-modules/matplotlib/default.nix-  # `$DISPLAY` is not set. The fallback option assumes that Tcl/Tk are both
pkgs/development/python-modules/matplotlib/default.nix-  # installed under the same path which is not true in Nix.
pkgs/development/python-modules/matplotlib/default.nix-  # With the following patch we just hard-code these paths into the install
pkgs/development/python-modules/matplotlib/default.nix-  # script.
pkgs/development/python-modules/matplotlib/default.nix-  postPatch = ''
pkgs/development/python-modules/matplotlib/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/matplotlib/default.nix-      --replace-fail "meson-python>=0.13.1,<0.17.0" meson-python
pkgs/development/python-modules/matplotlib/default.nix-
pkgs/development/python-modules/matplotlib/default.nix-    patchShebangs tools
pkgs/development/python-modules/matplotlib/default.nix-  ''
pkgs/development/python-modules/matplotlib/default.nix-  + lib.optionalString (stdenv.hostPlatform.isLinux && interactive) ''
pkgs/development/python-modules/matplotlib/default.nix-    # fix paths to libraries in dlopen calls (headless detection)
pkgs/development/python-modules/matplotlib/default.nix:    substituteInPlace src/_c_internal_utils.cpp \
pkgs/development/python-modules/matplotlib/default.nix-      --replace-fail libX11.so.6 ${libX11}/lib/libX11.so.6 \
pkgs/development/python-modules/matplotlib/default.nix-      --replace-fail libwayland-client.so.0 ${wayland}/lib/libwayland-client.so.0
pkgs/development/python-modules/matplotlib/default.nix-  '';
pkgs/development/python-modules/matplotlib/default.nix-
--
pkgs/development/python-modules/django-prometheus/default.nix-
pkgs/development/python-modules/django-prometheus/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/django-prometheus/default.nix-    owner = "django-commons";
pkgs/development/python-modules/django-prometheus/default.nix-    repo = "django-prometheus";
pkgs/development/python-modules/django-prometheus/default.nix-    tag = "v${version}";
pkgs/development/python-modules/django-prometheus/default.nix-    hash = "sha256-Bf1JSh9ibiPOa252IPld1FvHTPbCsB/amtlQdRQwoWY=";
pkgs/development/python-modules/django-prometheus/default.nix-  };
pkgs/development/python-modules/django-prometheus/default.nix-
pkgs/development/python-modules/django-prometheus/default.nix-  postPatch = ''
pkgs/development/python-modules/django-prometheus/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/django-prometheus/default.nix-      --replace-fail "setuptools >= 67.7.2, < 72.0.0" setuptools
pkgs/development/python-modules/django-prometheus/default.nix-
pkgs/development/python-modules/django-prometheus/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/django-prometheus/default.nix-      --replace-fail '"pytest-runner"' ""
pkgs/development/python-modules/django-prometheus/default.nix-  '';
pkgs/development/python-modules/django-prometheus/default.nix-
pkgs/development/python-modules/django-prometheus/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/django-prometheus/default.nix-
pkgs/development/python-modules/django-prometheus/default.nix-  dependencies = [ prometheus-client ];
pkgs/development/python-modules/django-prometheus/default.nix-
pkgs/development/python-modules/django-prometheus/default.nix-  pythonImportsCheck = [ "django_prometheus" ];
--
pkgs/development/python-modules/zope-contenttype/default.nix-
pkgs/development/python-modules/zope-contenttype/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/zope-contenttype/default.nix-    owner = "zopefoundation";
pkgs/development/python-modules/zope-contenttype/default.nix-    repo = "zope.contenttype";
pkgs/development/python-modules/zope-contenttype/default.nix-    tag = version;
pkgs/development/python-modules/zope-contenttype/default.nix-    hash = "sha256-mY6LlJn44hUfXpxEa99U6FNcsV9xJbR5w/iIS6hG+m4=";
pkgs/development/python-modules/zope-contenttype/default.nix-  };
pkgs/development/python-modules/zope-contenttype/default.nix-
pkgs/development/python-modules/zope-contenttype/default.nix-  postPatch = ''
pkgs/development/python-modules/zope-contenttype/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/zope-contenttype/default.nix-      --replace-fail "setuptools <= 75.6.0" setuptools
pkgs/development/python-modules/zope-contenttype/default.nix-  '';
pkgs/development/python-modules/zope-contenttype/default.nix-
pkgs/development/python-modules/zope-contenttype/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/zope-contenttype/default.nix-
pkgs/development/python-modules/zope-contenttype/default.nix-  nativeCheckInputs = [ pytestCheckHook ];
pkgs/development/python-modules/zope-contenttype/default.nix-
pkgs/development/python-modules/zope-contenttype/default.nix-  pythonImportsCheck = [ "zope.contenttype" ];
pkgs/development/python-modules/zope-contenttype/default.nix-
pkgs/development/python-modules/zope-contenttype/default.nix-  pythonNamespaces = [ "zope" ];
--
--
pkgs/development/python-modules/warrant/default.nix-    (fetchpatch {
pkgs/development/python-modules/warrant/default.nix-      name = "fix-pip10-compat.patch";
pkgs/development/python-modules/warrant/default.nix-      url = "https://github.com/capless/warrant/commit/ae17d17d9888b9218a8facf6f6ad0bf4adae9a12.patch";
pkgs/development/python-modules/warrant/default.nix-      sha256 = "1lvqi2qfa3kxdz05ab2lc7xnd3piyvvnz9kla2jl4pchi876z17c";
pkgs/development/python-modules/warrant/default.nix-    })
pkgs/development/python-modules/warrant/default.nix-  ];
pkgs/development/python-modules/warrant/default.nix-
pkgs/development/python-modules/warrant/default.nix-  # this needs to go when 0.6.2 or later is released
pkgs/development/python-modules/warrant/default.nix-  postPatch = ''
pkgs/development/python-modules/warrant/default.nix:    substituteInPlace requirements.txt \
pkgs/development/python-modules/warrant/default.nix-      --replace "python-jose-cryptodome>=1.3.2" "python-jose>=2.0.0"
pkgs/development/python-modules/warrant/default.nix-  '';
pkgs/development/python-modules/warrant/default.nix-
pkgs/development/python-modules/warrant/default.nix-  nativeCheckInputs = [ mock ];
pkgs/development/python-modules/warrant/default.nix-
pkgs/development/python-modules/warrant/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/warrant/default.nix-    boto3
pkgs/development/python-modules/warrant/default.nix-    envs
pkgs/development/python-modules/warrant/default.nix-    python-jose
pkgs/development/python-modules/warrant/default.nix-    requests
--
--
pkgs/development/python-modules/flask-dramatiq/default.nix-
pkgs/development/python-modules/flask-dramatiq/default.nix-  src = fetchFromGitLab {
pkgs/development/python-modules/flask-dramatiq/default.nix-    owner = "bersace";
pkgs/development/python-modules/flask-dramatiq/default.nix-    repo = "flask-dramatiq";
pkgs/development/python-modules/flask-dramatiq/default.nix-    rev = "840209e9bf582b4dda468e8bba515f248f3f8534";
pkgs/development/python-modules/flask-dramatiq/default.nix-    hash = "sha256-qjV1zyVzHPXMt+oUeGBdP9XVlbcSz2MF9Zygj543T4w=";
pkgs/development/python-modules/flask-dramatiq/default.nix-  };
pkgs/development/python-modules/flask-dramatiq/default.nix-
pkgs/development/python-modules/flask-dramatiq/default.nix-  postPatch = ''
pkgs/development/python-modules/flask-dramatiq/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/flask-dramatiq/default.nix-      --replace 'poetry>=0.12' 'poetry-core' \
pkgs/development/python-modules/flask-dramatiq/default.nix-      --replace 'poetry.masonry.api' 'poetry.core.masonry.api'
pkgs/development/python-modules/flask-dramatiq/default.nix-
pkgs/development/python-modules/flask-dramatiq/default.nix-    patchShebangs --build ./example.py
pkgs/development/python-modules/flask-dramatiq/default.nix-  '';
pkgs/development/python-modules/flask-dramatiq/default.nix-
pkgs/development/python-modules/flask-dramatiq/default.nix-  build-system = [ poetry-core ];
pkgs/development/python-modules/flask-dramatiq/default.nix-
pkgs/development/python-modules/flask-dramatiq/default.nix-  dependencies = [ dramatiq ];
pkgs/development/python-modules/flask-dramatiq/default.nix-
--
--
pkgs/development/python-modules/logfury/default.nix-
pkgs/development/python-modules/logfury/default.nix-  nativeBuildInputs = [ setuptools-scm ];
pkgs/development/python-modules/logfury/default.nix-
pkgs/development/python-modules/logfury/default.nix-  nativeCheckInputs = [
pkgs/development/python-modules/logfury/default.nix-    pytestCheckHook
pkgs/development/python-modules/logfury/default.nix-    testfixtures
pkgs/development/python-modules/logfury/default.nix-  ];
pkgs/development/python-modules/logfury/default.nix-
pkgs/development/python-modules/logfury/default.nix-  postPatch = ''
pkgs/development/python-modules/logfury/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/logfury/default.nix-      --replace "'setuptools_scm<6.0'" "'setuptools_scm'"
pkgs/development/python-modules/logfury/default.nix-  '';
pkgs/development/python-modules/logfury/default.nix-
pkgs/development/python-modules/logfury/default.nix-  pythonImportsCheck = [ "logfury" ];
pkgs/development/python-modules/logfury/default.nix-
pkgs/development/python-modules/logfury/default.nix-  meta = with lib; {
pkgs/development/python-modules/logfury/default.nix-    description = "Python module that allows for responsible, low-boilerplate logging of method calls";
pkgs/development/python-modules/logfury/default.nix-    homepage = "https://github.com/ppolewicz/logfury";
pkgs/development/python-modules/logfury/default.nix-    license = licenses.bsd3;
pkgs/development/python-modules/logfury/default.nix-    maintainers = with maintainers; [ jwiegley ];
--
--
pkgs/development/python-modules/patool/default.nix-    hash = "sha256-KAOJi8vUP9kPa++dLEXf3mwrv1kmV7uDZmtvngPxQ90=";
pkgs/development/python-modules/patool/default.nix-  };
pkgs/development/python-modules/patool/default.nix-
pkgs/development/python-modules/patool/default.nix-  postPatch = ''
pkgs/development/python-modules/patool/default.nix:    substituteInPlace patoolib/util.py \
pkgs/development/python-modules/patool/default.nix-      --replace-fail 'path = os.environ.get("PATH", os.defpath)' 'path = os.environ.get("PATH", os.defpath) + ":${lib.makeBinPath compression-utilities}"'
pkgs/development/python-modules/patool/default.nix-  '';
pkgs/development/python-modules/patool/default.nix-
pkgs/development/python-modules/patool/default.nix-  postInstall = lib.optionalString (stdenv.buildPlatform.canExecute stdenv.hostPlatform) ''
pkgs/development/python-modules/patool/default.nix-    installShellCompletion --cmd patool \
pkgs/development/python-modules/patool/default.nix-      --bash <(${argcomplete}/bin/register-python-argcomplete -s bash $out/bin/patool) \
pkgs/development/python-modules/patool/default.nix-      --fish <(${argcomplete}/bin/register-python-argcomplete -s fish $out/bin/patool) \
pkgs/development/python-modules/patool/default.nix-      --zsh <(${argcomplete}/bin/register-python-argcomplete -s zsh $out/bin/patool)
pkgs/development/python-modules/patool/default.nix-  '';
pkgs/development/python-modules/patool/default.nix-
--
pkgs/development/python-modules/zope-cachedescriptors/default.nix-  pyproject = true;
pkgs/development/python-modules/zope-cachedescriptors/default.nix-
pkgs/development/python-modules/zope-cachedescriptors/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/zope-cachedescriptors/default.nix-    owner = "zopefoundation";
pkgs/development/python-modules/zope-cachedescriptors/default.nix-    repo = "zope.cachedescriptors";
pkgs/development/python-modules/zope-cachedescriptors/default.nix-    tag = version;
pkgs/development/python-modules/zope-cachedescriptors/default.nix-    hash = "sha256-2cb8XosPCAV2BfMisCN9mr0KIu5xcsLPIcPkmpeVT+k=";
pkgs/development/python-modules/zope-cachedescriptors/default.nix-  };
pkgs/development/python-modules/zope-cachedescriptors/default.nix-
pkgs/development/python-modules/zope-cachedescriptors/default.nix-  postPatch = ''
pkgs/development/python-modules/zope-cachedescriptors/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/zope-cachedescriptors/default.nix-      --replace-fail "setuptools <= 75.6.0" setuptools
pkgs/development/python-modules/zope-cachedescriptors/default.nix-  '';
pkgs/development/python-modules/zope-cachedescriptors/default.nix-
pkgs/development/python-modules/zope-cachedescriptors/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/zope-cachedescriptors/default.nix-
pkgs/development/python-modules/zope-cachedescriptors/default.nix-  dependencies = [ setuptools ];
pkgs/development/python-modules/zope-cachedescriptors/default.nix-
pkgs/development/python-modules/zope-cachedescriptors/default.nix-  nativeCheckInputs = [ pytestCheckHook ];
pkgs/development/python-modules/zope-cachedescriptors/default.nix-
pkgs/development/python-modules/zope-cachedescriptors/default.nix-  enabledTestPaths = [ "src/zope/cachedescriptors/tests.py" ];
--
--
pkgs/development/python-modules/pelican/default.nix-    pandoc
--
pkgs/development/python-modules/paddle-bfloat/default.nix-
pkgs/development/python-modules/paddle-bfloat/default.nix-  src = fetchPypi {
pkgs/development/python-modules/paddle-bfloat/default.nix-    pname = "paddle_bfloat";
pkgs/development/python-modules/paddle-bfloat/default.nix-    inherit version;
pkgs/development/python-modules/paddle-bfloat/default.nix-    hash = "sha256-mrjQCtLsXOvqeHHMjuMx65FvMfZ2+wTh1ao9ZJE+9xw=";
pkgs/development/python-modules/paddle-bfloat/default.nix-  };
pkgs/development/python-modules/paddle-bfloat/default.nix-
pkgs/development/python-modules/paddle-bfloat/default.nix-  postPatch = ''
pkgs/development/python-modules/paddle-bfloat/default.nix-    sed '1i#include <memory>' -i bfloat16.cc # gcc12
pkgs/development/python-modules/paddle-bfloat/default.nix-    # replace deprecated function for python3.11
pkgs/development/python-modules/paddle-bfloat/default.nix:    substituteInPlace bfloat16.cc \
pkgs/development/python-modules/paddle-bfloat/default.nix-      --replace "Py_TYPE(&NPyBfloat16_Descr) = &PyArrayDescr_Type" "Py_SET_TYPE(&NPyBfloat16_Descr, &PyArrayDescr_Type)"
pkgs/development/python-modules/paddle-bfloat/default.nix-  '';
pkgs/development/python-modules/paddle-bfloat/default.nix-
pkgs/development/python-modules/paddle-bfloat/default.nix-  disabled = pythonOlder "3.9" || pythonAtLeast "3.12";
pkgs/development/python-modules/paddle-bfloat/default.nix-
pkgs/development/python-modules/paddle-bfloat/default.nix-  propagatedBuildInputs = [ numpy ];
pkgs/development/python-modules/paddle-bfloat/default.nix-
pkgs/development/python-modules/paddle-bfloat/default.nix-  pythonImportsCheck = [ "paddle_bfloat" ];
--
pkgs/development/python-modules/parsimonious/default.nix-  disabledTests = [
pkgs/development/python-modules/parsimonious/default.nix-    # test_benchmarks.py tests are actually benchmarks and may fail due to
pkgs/development/python-modules/parsimonious/default.nix-    # something being unexpectedly slow on a heavily loaded build machine
pkgs/development/python-modules/parsimonious/default.nix-    "test_lists_vs_dicts"
pkgs/development/python-modules/parsimonious/default.nix-    "test_call_vs_inline"
pkgs/development/python-modules/parsimonious/default.nix-    "test_startswith_vs_regex"
pkgs/development/python-modules/parsimonious/default.nix-  ];
pkgs/development/python-modules/parsimonious/default.nix-
pkgs/development/python-modules/parsimonious/default.nix-  postPatch = ''
pkgs/development/python-modules/parsimonious/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/parsimonious/default.nix-      --replace "regex>=2022.3.15" "regex"
pkgs/development/python-modules/parsimonious/default.nix-  '';
pkgs/development/python-modules/parsimonious/default.nix-
pkgs/development/python-modules/parsimonious/default.nix-  pythonImportsCheck = [
pkgs/development/python-modules/parsimonious/default.nix-    "parsimonious"
pkgs/development/python-modules/parsimonious/default.nix-    "parsimonious.grammar"
pkgs/development/python-modules/parsimonious/default.nix-    "parsimonious.nodes"
pkgs/development/python-modules/parsimonious/default.nix-  ];
pkgs/development/python-modules/parsimonious/default.nix-
pkgs/development/python-modules/parsimonious/default.nix-  meta = with lib; {
--
--
pkgs/development/python-modules/aws-request-signer/default.nix-  pyproject = true;
pkgs/development/python-modules/aws-request-signer/default.nix-
pkgs/development/python-modules/aws-request-signer/default.nix-  src = fetchPypi {
pkgs/development/python-modules/aws-request-signer/default.nix-    inherit version;
pkgs/development/python-modules/aws-request-signer/default.nix-    pname = "aws_request_signer";
pkgs/development/python-modules/aws-request-signer/default.nix-    hash = "sha256-DVorDO0wz94Fhduax7VsQZ5B5SnBfsHQoLoW4m6Ce+U=";
pkgs/development/python-modules/aws-request-signer/default.nix-  };
pkgs/development/python-modules/aws-request-signer/default.nix-
pkgs/development/python-modules/aws-request-signer/default.nix-  postPatch = ''
pkgs/development/python-modules/aws-request-signer/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/aws-request-signer/default.nix-      --replace-fail "poetry>=0.12" poetry-core \
pkgs/development/python-modules/aws-request-signer/default.nix-      --replace-fail poetry.masonry.api poetry.core.masonry.api
pkgs/development/python-modules/aws-request-signer/default.nix-  '';
pkgs/development/python-modules/aws-request-signer/default.nix-
pkgs/development/python-modules/aws-request-signer/default.nix-  build-system = [ poetry-core ];
pkgs/development/python-modules/aws-request-signer/default.nix-
pkgs/development/python-modules/aws-request-signer/default.nix-  dependencies = [
pkgs/development/python-modules/aws-request-signer/default.nix-    requests
pkgs/development/python-modules/aws-request-signer/default.nix-    requests-toolbelt
pkgs/development/python-modules/aws-request-signer/default.nix-  ];
--
pkgs/development/python-modules/merkletools/default.nix-
pkgs/development/python-modules/merkletools/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/merkletools/default.nix-    owner = "Tierion";
pkgs/development/python-modules/merkletools/default.nix-    repo = "pymerkletools";
pkgs/development/python-modules/merkletools/default.nix-    tag = version;
pkgs/development/python-modules/merkletools/default.nix-    hash = "sha256-pd7Wxi7Sk95RcrFOTOtl725nIXidva3ftdKSGxHYPTA=";
pkgs/development/python-modules/merkletools/default.nix-  };
pkgs/development/python-modules/merkletools/default.nix-
pkgs/development/python-modules/merkletools/default.nix-  postPatch = ''
pkgs/development/python-modules/merkletools/default.nix-    # pysha3 is deprecated and not needed for Python > 3.6
pkgs/development/python-modules/merkletools/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/merkletools/default.nix-      --replace "install_requires=install_requires" "install_requires=[],"
pkgs/development/python-modules/merkletools/default.nix-  '';
pkgs/development/python-modules/merkletools/default.nix-
pkgs/development/python-modules/merkletools/default.nix-  checkInputs = [ pytestCheckHook ];
pkgs/development/python-modules/merkletools/default.nix-
pkgs/development/python-modules/merkletools/default.nix-  pythonImportsCheck = [ "merkletools" ];
pkgs/development/python-modules/merkletools/default.nix-
pkgs/development/python-modules/merkletools/default.nix-  meta = with lib; {
pkgs/development/python-modules/merkletools/default.nix-    description = "Python tools for creating Merkle trees, generating Merkle proofs, and verification of Merkle proofs";
--
pkgs/development/python-modules/pythreejs/default.nix-  };
pkgs/development/python-modules/pythreejs/default.nix-
pkgs/development/python-modules/pythreejs/default.nix-  build-system = [
pkgs/development/python-modules/pythreejs/default.nix-    jupyterlab
pkgs/development/python-modules/pythreejs/default.nix-    setuptools
pkgs/development/python-modules/pythreejs/default.nix-  ];
pkgs/development/python-modules/pythreejs/default.nix-
pkgs/development/python-modules/pythreejs/default.nix-  # It seems pythonRelaxDeps doesn't work for these
pkgs/development/python-modules/pythreejs/default.nix-  postPatch = ''
pkgs/development/python-modules/pythreejs/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/pythreejs/default.nix-      --replace-fail "jupyterlab~=" "jupyterlab>="
pkgs/development/python-modules/pythreejs/default.nix-
pkgs/development/python-modules/pythreejs/default.nix-    # https://github.com/jupyter-widgets/pythreejs/pull/420
pkgs/development/python-modules/pythreejs/default.nix:    substituteInPlace setupbase.py \
pkgs/development/python-modules/pythreejs/default.nix-      --replace-fail "import pipes" "" \
pkgs/development/python-modules/pythreejs/default.nix-      --replace-fail "pipes.quote" "shlex.quote"
pkgs/development/python-modules/pythreejs/default.nix-  '';
pkgs/development/python-modules/pythreejs/default.nix-
pkgs/development/python-modules/pythreejs/default.nix-  # Don't run npm install, all files are already where they should be present.
pkgs/development/python-modules/pythreejs/default.nix-  # If we would run npm install, npm would detect package-lock.json is an old format,
pkgs/development/python-modules/pythreejs/default.nix-  # and try to fetch more metadata from the registry, which cannot work in the sandbox.
--
pkgs/development/python-modules/bumpfontversion/default.nix-
pkgs/development/python-modules/bumpfontversion/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/bumpfontversion/default.nix-    owner = "simoncozens";
pkgs/development/python-modules/bumpfontversion/default.nix-    repo = "bumpfontversion";
pkgs/development/python-modules/bumpfontversion/default.nix-    tag = "v${version}";
pkgs/development/python-modules/bumpfontversion/default.nix-    hash = "sha256-qcKZGv/KeeSRBq4SdnuZlurp0CUs40iEQjw9/1LltUg=";
pkgs/development/python-modules/bumpfontversion/default.nix-  };
pkgs/development/python-modules/bumpfontversion/default.nix-
pkgs/development/python-modules/bumpfontversion/default.nix-  postPatch = ''
pkgs/development/python-modules/bumpfontversion/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/bumpfontversion/default.nix-      --replace-fail 'poetry>=' 'poetry-core>=' \
pkgs/development/python-modules/bumpfontversion/default.nix-      --replace-fail 'poetry.masonry.api' 'poetry.core.masonry.api'
pkgs/development/python-modules/bumpfontversion/default.nix-  '';
pkgs/development/python-modules/bumpfontversion/default.nix-
pkgs/development/python-modules/bumpfontversion/default.nix-  nativeBuildInputs = [ pythonRelaxDepsHook ];
pkgs/development/python-modules/bumpfontversion/default.nix-
pkgs/development/python-modules/bumpfontversion/default.nix-  pythonRelaxDeps = [ "glyphslib" ];
pkgs/development/python-modules/bumpfontversion/default.nix-
pkgs/development/python-modules/bumpfontversion/default.nix-  build-system = [ poetry-core ];
pkgs/development/python-modules/bumpfontversion/default.nix-
--
--
pkgs/development/python-modules/voip-utils/default.nix-
pkgs/development/python-modules/voip-utils/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/voip-utils/default.nix-    owner = "home-assistant-libs";
pkgs/development/python-modules/voip-utils/default.nix-    repo = "voip-utils";
pkgs/development/python-modules/voip-utils/default.nix-    tag = "v${version}";
pkgs/development/python-modules/voip-utils/default.nix-    hash = "sha256-vFzSDK5n5qhhUL1Lxy0R1iuB+uUovCzZFV5wPIt8cek=";
pkgs/development/python-modules/voip-utils/default.nix-  };
pkgs/development/python-modules/voip-utils/default.nix-
pkgs/development/python-modules/voip-utils/default.nix-  postPatch = ''
pkgs/development/python-modules/voip-utils/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/voip-utils/default.nix-      --replace-fail "~=" ">="
pkgs/development/python-modules/voip-utils/default.nix-  '';
pkgs/development/python-modules/voip-utils/default.nix-
pkgs/development/python-modules/voip-utils/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/voip-utils/default.nix-
pkgs/development/python-modules/voip-utils/default.nix-  pythonRelaxDeps = [ "opuslib" ];
pkgs/development/python-modules/voip-utils/default.nix-
pkgs/development/python-modules/voip-utils/default.nix-  dependencies = [ opuslib ];
pkgs/development/python-modules/voip-utils/default.nix-
pkgs/development/python-modules/voip-utils/default.nix-  pythonImportsCheck = [ "voip_utils" ];
--
--
pkgs/development/python-modules/ipytablewidgets/default.nix-    inherit pname version;
pkgs/development/python-modules/ipytablewidgets/default.nix-    hash = "sha256-CGkb//mLUmkyv+hmVJX5+04JGCfw+TtfBxMTXW0bhsw=";
pkgs/development/python-modules/ipytablewidgets/default.nix-  };
pkgs/development/python-modules/ipytablewidgets/default.nix-
pkgs/development/python-modules/ipytablewidgets/default.nix-  # Opened https://github.com/progressivis/ipytablewidgets/issues/3 to ask if
pkgs/development/python-modules/ipytablewidgets/default.nix-  # jupyterlab can be updated upstream. (From commits, it looks like it was
pkgs/development/python-modules/ipytablewidgets/default.nix-  # set to this version on purpose.) In the meantime, the build still works.
pkgs/development/python-modules/ipytablewidgets/default.nix-  #
pkgs/development/python-modules/ipytablewidgets/default.nix-  postPatch = ''
pkgs/development/python-modules/ipytablewidgets/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/ipytablewidgets/default.nix-      --replace 'jupyterlab>=3.0.0,<3.7' 'jupyterlab>=3.0.0'
pkgs/development/python-modules/ipytablewidgets/default.nix-  '';
pkgs/development/python-modules/ipytablewidgets/default.nix-
pkgs/development/python-modules/ipytablewidgets/default.nix-  build-system = [
pkgs/development/python-modules/ipytablewidgets/default.nix-    jupyter-packaging
pkgs/development/python-modules/ipytablewidgets/default.nix-    jupyterlab
pkgs/development/python-modules/ipytablewidgets/default.nix-    setuptools
pkgs/development/python-modules/ipytablewidgets/default.nix-  ];
pkgs/development/python-modules/ipytablewidgets/default.nix-
pkgs/development/python-modules/ipytablewidgets/default.nix-  dependencies = [
--
--
pkgs/development/python-modules/urllib3/default.nix-      hash = "sha256-P8R3M8fkGdS8P2s9wrT4kLt0OQajDVa6Slv6S7/5J2A=";
pkgs/development/python-modules/urllib3/default.nix-    };
pkgs/development/python-modules/urllib3/default.nix-
pkgs/development/python-modules/urllib3/default.nix-    build-system = [
pkgs/development/python-modules/urllib3/default.nix-      hatchling
pkgs/development/python-modules/urllib3/default.nix-      hatch-vcs
pkgs/development/python-modules/urllib3/default.nix-    ];
pkgs/development/python-modules/urllib3/default.nix-
pkgs/development/python-modules/urllib3/default.nix-    postPatch = ''
pkgs/development/python-modules/urllib3/default.nix:      substituteInPlace pyproject.toml \
pkgs/development/python-modules/urllib3/default.nix-        --replace-fail ', "setuptools-scm>=8,<9"' ""
pkgs/development/python-modules/urllib3/default.nix-    '';
pkgs/development/python-modules/urllib3/default.nix-
pkgs/development/python-modules/urllib3/default.nix-    optional-dependencies = {
pkgs/development/python-modules/urllib3/default.nix-      brotli = if isPyPy then [ brotlicffi ] else [ brotli ];
pkgs/development/python-modules/urllib3/default.nix-      socks = [ pysocks ];
pkgs/development/python-modules/urllib3/default.nix-      zstd = [ zstandard ];
pkgs/development/python-modules/urllib3/default.nix-    };
pkgs/development/python-modules/urllib3/default.nix-
pkgs/development/python-modules/urllib3/default.nix-    nativeCheckInputs = [
--
--
pkgs/development/python-modules/whey/default.nix-
pkgs/development/python-modules/whey/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/whey/default.nix-    owner = "repo-helper";
pkgs/development/python-modules/whey/default.nix-    repo = "whey";
pkgs/development/python-modules/whey/default.nix-    tag = "v${version}";
pkgs/development/python-modules/whey/default.nix-    hash = "sha256-s2jZmuFj0gTWVTcXWcBhcu5RBuaf/qMS/xzIpIoG1ZE=";
pkgs/development/python-modules/whey/default.nix-  };
pkgs/development/python-modules/whey/default.nix-
pkgs/development/python-modules/whey/default.nix-  postPatch = ''
pkgs/development/python-modules/whey/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/whey/default.nix-      --replace-fail 'setuptools!=61.*,<=67.1.0,>=40.6.0' setuptools
pkgs/development/python-modules/whey/default.nix-  '';
pkgs/development/python-modules/whey/default.nix-
pkgs/development/python-modules/whey/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/whey/default.nix-
pkgs/development/python-modules/whey/default.nix-  dependencies = [
pkgs/development/python-modules/whey/default.nix-    attrs
pkgs/development/python-modules/whey/default.nix-    click
pkgs/development/python-modules/whey/default.nix-    consolekit
pkgs/development/python-modules/whey/default.nix-    dist-meta
--
--
pkgs/development/python-modules/serverlessrepo/default.nix-  ];
pkgs/development/python-modules/serverlessrepo/default.nix-
pkgs/development/python-modules/serverlessrepo/default.nix-  nativeCheckInputs = [
pkgs/development/python-modules/serverlessrepo/default.nix-    pytestCheckHook
pkgs/development/python-modules/serverlessrepo/default.nix-    mock
pkgs/development/python-modules/serverlessrepo/default.nix-  ];
pkgs/development/python-modules/serverlessrepo/default.nix-
pkgs/development/python-modules/serverlessrepo/default.nix-  postPatch = ''
pkgs/development/python-modules/serverlessrepo/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/serverlessrepo/default.nix-      --replace "pyyaml~=5.1" "pyyaml" \
pkgs/development/python-modules/serverlessrepo/default.nix-      --replace "boto3~=1.9, >=1.9.56" "boto3"
pkgs/development/python-modules/serverlessrepo/default.nix-  '';
pkgs/development/python-modules/serverlessrepo/default.nix-
pkgs/development/python-modules/serverlessrepo/default.nix-  enabledTestPaths = [ "tests/unit" ];
pkgs/development/python-modules/serverlessrepo/default.nix-
pkgs/development/python-modules/serverlessrepo/default.nix-  pythonImportsCheck = [ "serverlessrepo" ];
pkgs/development/python-modules/serverlessrepo/default.nix-
pkgs/development/python-modules/serverlessrepo/default.nix-  meta = with lib; {
pkgs/development/python-modules/serverlessrepo/default.nix-    homepage = "https://github.com/awslabs/aws-serverlessrepo-python";
--
pkgs/development/python-modules/versiontag/default.nix-  pyproject = true;
--
pkgs/development/python-modules/inkex/default.nix-    "tests/test_inkex_gui_listview.py"
pkgs/development/python-modules/inkex/default.nix-    "tests/test_inkex_gui_window.py"
pkgs/development/python-modules/inkex/default.nix-    # Failed to find pixmap 'image-missing' in /build/source/tests/data/
pkgs/development/python-modules/inkex/default.nix-    "tests/test_inkex_gui_pixmaps.py"
pkgs/development/python-modules/inkex/default.nix-  ];
pkgs/development/python-modules/inkex/default.nix-
pkgs/development/python-modules/inkex/default.nix-  postPatch = ''
pkgs/development/python-modules/inkex/default.nix-    cd share/extensions
pkgs/development/python-modules/inkex/default.nix-
pkgs/development/python-modules/inkex/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/inkex/default.nix-      --replace-fail 'scour = "^0.37"' 'scour = ">=0.37"'
pkgs/development/python-modules/inkex/default.nix-  '';
pkgs/development/python-modules/inkex/default.nix-
pkgs/development/python-modules/inkex/default.nix-  meta = {
pkgs/development/python-modules/inkex/default.nix-    description = "Library for manipulating SVG documents which is the basis for Inkscape extensions";
pkgs/development/python-modules/inkex/default.nix-    homepage = "https://gitlab.com/inkscape/extensions";
pkgs/development/python-modules/inkex/default.nix-    license = lib.licenses.gpl2Plus;
pkgs/development/python-modules/inkex/default.nix-    maintainers = with lib.maintainers; [ dotlambda ];
pkgs/development/python-modules/inkex/default.nix-  };
pkgs/development/python-modules/inkex/default.nix-}
--
--
pkgs/development/python-modules/weconnect-mqtt/default.nix-    owner = "tillsteinbach";
pkgs/development/python-modules/weconnect-mqtt/default.nix-    repo = "WeConnect-mqtt";
pkgs/development/python-modules/weconnect-mqtt/default.nix-    tag = "v${version}";
pkgs/development/python-modules/weconnect-mqtt/default.nix-    hash = "sha256-jTScDPTj7aIQcGuL2g8MvuYln6iaj6abEyCfd8vvT2I=";
pkgs/development/python-modules/weconnect-mqtt/default.nix-  };
pkgs/development/python-modules/weconnect-mqtt/default.nix-
pkgs/development/python-modules/weconnect-mqtt/default.nix-  postPatch = ''
pkgs/development/python-modules/weconnect-mqtt/default.nix:    substituteInPlace weconnect_mqtt/__version.py \
pkgs/development/python-modules/weconnect-mqtt/default.nix-      --replace-fail "0.0.0dev" "${version}"
pkgs/development/python-modules/weconnect-mqtt/default.nix:    substituteInPlace requirements.txt \
pkgs/development/python-modules/weconnect-mqtt/default.nix-      --replace-fail "weconnect[Images]~=" "weconnect>="
pkgs/development/python-modules/weconnect-mqtt/default.nix:    substituteInPlace pytest.ini \
pkgs/development/python-modules/weconnect-mqtt/default.nix-      --replace-fail "required_plugins = pytest-cov" ""
pkgs/development/python-modules/weconnect-mqtt/default.nix-  '';
pkgs/development/python-modules/weconnect-mqtt/default.nix-
pkgs/development/python-modules/weconnect-mqtt/default.nix-  pythonRelaxDeps = [ "python-dateutil" ];
pkgs/development/python-modules/weconnect-mqtt/default.nix-
pkgs/development/python-modules/weconnect-mqtt/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/weconnect-mqtt/default.nix-
pkgs/development/python-modules/weconnect-mqtt/default.nix-  dependencies = [
pkgs/development/python-modules/weconnect-mqtt/default.nix-    paho-mqtt
--
pkgs/development/python-modules/kbcstorage/default.nix-
pkgs/development/python-modules/kbcstorage/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/kbcstorage/default.nix-    owner = "keboola";
pkgs/development/python-modules/kbcstorage/default.nix-    repo = "sapi-python-client";
pkgs/development/python-modules/kbcstorage/default.nix-    tag = version;
pkgs/development/python-modules/kbcstorage/default.nix-    hash = "sha256-30bAw5pYEUj0jeZWiJxzZ7lDs/+63tlcoLaHrUmYCs8=";
pkgs/development/python-modules/kbcstorage/default.nix-  };
pkgs/development/python-modules/kbcstorage/default.nix-
pkgs/development/python-modules/kbcstorage/default.nix-  postPatch = ''
pkgs/development/python-modules/kbcstorage/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/kbcstorage/default.nix-      --replace-fail "urllib3<2.0.0" "urllib3"
pkgs/development/python-modules/kbcstorage/default.nix-  '';
pkgs/development/python-modules/kbcstorage/default.nix-
pkgs/development/python-modules/kbcstorage/default.nix-  build-system = [
pkgs/development/python-modules/kbcstorage/default.nix-    setuptools
pkgs/development/python-modules/kbcstorage/default.nix-    setuptools-git-versioning
pkgs/development/python-modules/kbcstorage/default.nix-    setuptools-scm
pkgs/development/python-modules/kbcstorage/default.nix-  ];
pkgs/development/python-modules/kbcstorage/default.nix-
pkgs/development/python-modules/kbcstorage/default.nix-  pythonRelaxDeps = [
--
--
pkgs/development/python-modules/neo4j/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/neo4j/default.nix-    owner = "neo4j";
pkgs/development/python-modules/neo4j/default.nix-    repo = "neo4j-python-driver";
pkgs/development/python-modules/neo4j/default.nix-    tag = version;
pkgs/development/python-modules/neo4j/default.nix-    hash = "sha256-dQvQO+Re+ki9w+itzE6/WdiiLdMlU4yePt01vAPe4+M=";
pkgs/development/python-modules/neo4j/default.nix-  };
pkgs/development/python-modules/neo4j/default.nix-
pkgs/development/python-modules/neo4j/default.nix-  postPatch = ''
pkgs/development/python-modules/neo4j/default.nix-    # The dynamic versioning adds a postfix (.dev0) to the version
pkgs/development/python-modules/neo4j/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/neo4j/default.nix-      --replace-fail "setuptools ==" "setuptools >=" \
pkgs/development/python-modules/neo4j/default.nix-      --replace-fail "tomlkit ==" "tomlkit >=" \
pkgs/development/python-modules/neo4j/default.nix-      --replace-fail 'dynamic = ["version", "readme"]' 'dynamic = ["readme"]' \
pkgs/development/python-modules/neo4j/default.nix-      --replace-fail '#readme = "README.rst"' 'version = "${version}"'
pkgs/development/python-modules/neo4j/default.nix-  '';
pkgs/development/python-modules/neo4j/default.nix-
pkgs/development/python-modules/neo4j/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/neo4j/default.nix-
pkgs/development/python-modules/neo4j/default.nix-  dependencies = [
pkgs/development/python-modules/neo4j/default.nix-    pytz
--
pkgs/development/python-modules/p1monitor/default.nix-  disabled = pythonOlder "3.11";
--
pkgs/development/python-modules/pygreat/default.nix-    owner = "greatscottgadgets";
pkgs/development/python-modules/pygreat/default.nix-    repo = "libgreat";
pkgs/development/python-modules/pygreat/default.nix-    tag = "v${version}";
pkgs/development/python-modules/pygreat/default.nix-    hash = "sha256-2PFeCG7m8qiK3eBX2838P6ZsLoQxcJBG+/TppUMT6dE=";
pkgs/development/python-modules/pygreat/default.nix-  };
pkgs/development/python-modules/pygreat/default.nix-
pkgs/development/python-modules/pygreat/default.nix-  sourceRoot = "${src.name}/host";
pkgs/development/python-modules/pygreat/default.nix-
pkgs/development/python-modules/pygreat/default.nix-  postPatch = ''
pkgs/development/python-modules/pygreat/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/pygreat/default.nix-      --replace-fail '"setuptools-git-versioning<2"' "" \
pkgs/development/python-modules/pygreat/default.nix-      --replace-fail 'dynamic = ["version"]' 'version = "${version}"'
pkgs/development/python-modules/pygreat/default.nix-  '';
pkgs/development/python-modules/pygreat/default.nix-
pkgs/development/python-modules/pygreat/default.nix-  pythonRemoveDeps = [ "backports.functools_lru_cache" ];
pkgs/development/python-modules/pygreat/default.nix-
pkgs/development/python-modules/pygreat/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/pygreat/default.nix-
pkgs/development/python-modules/pygreat/default.nix-  dependencies = [ pyusb ];
pkgs/development/python-modules/pygreat/default.nix-
--
--
pkgs/development/python-modules/metawear/default.nix-  buildInputs = [
pkgs/development/python-modules/metawear/default.nix-    boost
pkgs/development/python-modules/metawear/default.nix-    bluez
pkgs/development/python-modules/metawear/default.nix-    nlohmann_json
pkgs/development/python-modules/metawear/default.nix-  ];
pkgs/development/python-modules/metawear/default.nix-
pkgs/development/python-modules/metawear/default.nix-  postPatch = ''
pkgs/development/python-modules/metawear/default.nix-    # remove vendored nlohmann_json
pkgs/development/python-modules/metawear/default.nix-    rm MetaWear-SDK-Cpp/src/metawear/dfu/cpp/json.hpp
pkgs/development/python-modules/metawear/default.nix:    substituteInPlace MetaWear-SDK-Cpp/src/metawear/dfu/cpp/file_operations.cpp \
pkgs/development/python-modules/metawear/default.nix-        --replace '#include "json.hpp"' '#include <nlohmann/json.hpp>'
pkgs/development/python-modules/metawear/default.nix-  '';
pkgs/development/python-modules/metawear/default.nix-
pkgs/development/python-modules/metawear/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/metawear/default.nix-    pyserial
pkgs/development/python-modules/metawear/default.nix-    requests
pkgs/development/python-modules/metawear/default.nix-    warble
pkgs/development/python-modules/metawear/default.nix-  ];
pkgs/development/python-modules/metawear/default.nix-
pkgs/development/python-modules/metawear/default.nix-  enableParallelBuilding = true;
--
--
pkgs/development/python-modules/trectools/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/trectools/default.nix-    owner = "joaopalotti";
pkgs/development/python-modules/trectools/default.nix-    repo = "trectools";
pkgs/development/python-modules/trectools/default.nix-    # https://github.com/joaopalotti/trectools/issues/41
pkgs/development/python-modules/trectools/default.nix-    rev = "8a896def007e3d657eb29f820ee3de98e2f32691";
pkgs/development/python-modules/trectools/default.nix-    hash = "sha256-p8BvLO+rD/l+ATE4+u3I6k25R1RVKlk2dn+RLQZTLDs=";
pkgs/development/python-modules/trectools/default.nix-  };
pkgs/development/python-modules/trectools/default.nix-
pkgs/development/python-modules/trectools/default.nix-  postPatch = ''
pkgs/development/python-modules/trectools/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/trectools/default.nix-      --replace-fail "bs4 >= 0.0.0.1" "beautifulsoup4 >= 4.11.1"
pkgs/development/python-modules/trectools/default.nix-  '';
pkgs/development/python-modules/trectools/default.nix-
pkgs/development/python-modules/trectools/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/trectools/default.nix-
pkgs/development/python-modules/trectools/default.nix-  dependencies = [
pkgs/development/python-modules/trectools/default.nix-    pandas
pkgs/development/python-modules/trectools/default.nix-    numpy
pkgs/development/python-modules/trectools/default.nix-    scikit-learn
pkgs/development/python-modules/trectools/default.nix-    scipy
--
pkgs/development/python-modules/pyscaffold/default.nix-    hash = "sha256-QIW43pIAufMZ32+Op5lyiPFZqOSyhLBi2bKk1qnBI0w=";
pkgs/development/python-modules/pyscaffold/default.nix-  };
pkgs/development/python-modules/pyscaffold/default.nix-
pkgs/development/python-modules/pyscaffold/default.nix-  nativeBuildInputs = [
pkgs/development/python-modules/pyscaffold/default.nix-    setuptools
pkgs/development/python-modules/pyscaffold/default.nix-    setuptools-scm
pkgs/development/python-modules/pyscaffold/default.nix-    wheel
pkgs/development/python-modules/pyscaffold/default.nix-  ];
pkgs/development/python-modules/pyscaffold/default.nix-
pkgs/development/python-modules/pyscaffold/default.nix-  postPatch = ''
pkgs/development/python-modules/pyscaffold/default.nix:    substituteInPlace setup.cfg --replace "platformdirs>=2,<4" "platformdirs"
pkgs/development/python-modules/pyscaffold/default.nix-  '';
pkgs/development/python-modules/pyscaffold/default.nix-
pkgs/development/python-modules/pyscaffold/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/pyscaffold/default.nix-    colorama
pkgs/development/python-modules/pyscaffold/default.nix-    configupdater
pkgs/development/python-modules/pyscaffold/default.nix-    importlib-metadata
pkgs/development/python-modules/pyscaffold/default.nix-    packaging
pkgs/development/python-modules/pyscaffold/default.nix-    platformdirs
pkgs/development/python-modules/pyscaffold/default.nix-    setuptools
pkgs/development/python-modules/pyscaffold/default.nix-    setuptools-scm
--
pkgs/development/python-modules/aionotion/default.nix-
pkgs/development/python-modules/aionotion/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/aionotion/default.nix-    owner = "bachya";
pkgs/development/python-modules/aionotion/default.nix-    repo = "aionotion";
pkgs/development/python-modules/aionotion/default.nix-    tag = version;
pkgs/development/python-modules/aionotion/default.nix-    hash = "sha256-MqH3CPp+dAX5DXtnHio95KGQ+Ok2TXrX6rn/AMx5OsY=";
pkgs/development/python-modules/aionotion/default.nix-  };
pkgs/development/python-modules/aionotion/default.nix-
pkgs/development/python-modules/aionotion/default.nix-  postPatch = ''
pkgs/development/python-modules/aionotion/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/aionotion/default.nix-      --replace-fail "poetry-core==" "poetry-core>="
pkgs/development/python-modules/aionotion/default.nix-  '';
pkgs/development/python-modules/aionotion/default.nix-
pkgs/development/python-modules/aionotion/default.nix-  nativeBuildInputs = [ poetry-core ];
pkgs/development/python-modules/aionotion/default.nix-
pkgs/development/python-modules/aionotion/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/aionotion/default.nix-    aiohttp
pkgs/development/python-modules/aionotion/default.nix-    certifi
pkgs/development/python-modules/aionotion/default.nix-    ciso8601
pkgs/development/python-modules/aionotion/default.nix-    frozenlist
--
--
pkgs/development/python-modules/whey-pth/default.nix-
pkgs/development/python-modules/whey-pth/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/whey-pth/default.nix-    owner = "repo-helper";
pkgs/development/python-modules/whey-pth/default.nix-    repo = "whey-pth";
pkgs/development/python-modules/whey-pth/default.nix-    tag = "v${version}";
pkgs/development/python-modules/whey-pth/default.nix-    hash = "sha256-A+bXB9F8FD+A1iRuETIxP12bkH/5NKcx01ERXJZAj+Q=";
pkgs/development/python-modules/whey-pth/default.nix-  };
pkgs/development/python-modules/whey-pth/default.nix-
pkgs/development/python-modules/whey-pth/default.nix-  postPatch = ''
pkgs/development/python-modules/whey-pth/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/whey-pth/default.nix-      --replace-fail 'setuptools!=61.*,<=67.1.0,>=40.6.0' setuptools
pkgs/development/python-modules/whey-pth/default.nix-  '';
pkgs/development/python-modules/whey-pth/default.nix-
pkgs/development/python-modules/whey-pth/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/whey-pth/default.nix-
pkgs/development/python-modules/whey-pth/default.nix-  dependencies = [
pkgs/development/python-modules/whey-pth/default.nix-    dom-toml
pkgs/development/python-modules/whey-pth/default.nix-    whey
pkgs/development/python-modules/whey-pth/default.nix-  ];
pkgs/development/python-modules/whey-pth/default.nix-
--
--
pkgs/development/python-modules/zope-deprecation/default.nix-
pkgs/development/python-modules/zope-deprecation/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/zope-deprecation/default.nix-    owner = "zopefoundation";
pkgs/development/python-modules/zope-deprecation/default.nix-    repo = "zope.deprecation";
pkgs/development/python-modules/zope-deprecation/default.nix-    tag = version;
pkgs/development/python-modules/zope-deprecation/default.nix-    hash = "sha256-5gqZuO3fGXkQl493QrvK7gl77mDteUp7tpo4DhSRI+o=";
pkgs/development/python-modules/zope-deprecation/default.nix-  };
pkgs/development/python-modules/zope-deprecation/default.nix-
pkgs/development/python-modules/zope-deprecation/default.nix-  postPatch = ''
pkgs/development/python-modules/zope-deprecation/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/zope-deprecation/default.nix-      --replace-fail "setuptools <= 75.6.0" "setuptools"
pkgs/development/python-modules/zope-deprecation/default.nix-  '';
pkgs/development/python-modules/zope-deprecation/default.nix-
pkgs/development/python-modules/zope-deprecation/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/zope-deprecation/default.nix-
pkgs/development/python-modules/zope-deprecation/default.nix-  nativeCheckInputs = [ pytestCheckHook ];
pkgs/development/python-modules/zope-deprecation/default.nix-
pkgs/development/python-modules/zope-deprecation/default.nix-  enabledTestPaths = [ "src/zope/deprecation/tests.py" ];
pkgs/development/python-modules/zope-deprecation/default.nix-
pkgs/development/python-modules/zope-deprecation/default.nix-  pythonImportsCheck = [ "zope.deprecation" ];
--
--
pkgs/development/python-modules/flask-appbuilder/default.nix-    python-dateutil
pkgs/development/python-modules/flask-appbuilder/default.nix-    prison
pkgs/development/python-modules/flask-appbuilder/default.nix-    pyjwt
pkgs/development/python-modules/flask-appbuilder/default.nix-    pyyaml
pkgs/development/python-modules/flask-appbuilder/default.nix-    sqlalchemy-utils
pkgs/development/python-modules/flask-appbuilder/default.nix-  ]
pkgs/development/python-modules/flask-appbuilder/default.nix-  ++ apispec.optional-dependencies.yaml;
pkgs/development/python-modules/flask-appbuilder/default.nix-
pkgs/development/python-modules/flask-appbuilder/default.nix-  postPatch = ''
pkgs/development/python-modules/flask-appbuilder/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/flask-appbuilder/default.nix-      --replace "apispec[yaml]>=3.3, <6" "apispec[yaml]" \
pkgs/development/python-modules/flask-appbuilder/default.nix-      --replace "Flask-SQLAlchemy>=2.4, <3" "Flask-SQLAlchemy" \
pkgs/development/python-modules/flask-appbuilder/default.nix-      --replace "Flask-Babel>=1, <3" "Flask-Babel" \
pkgs/development/python-modules/flask-appbuilder/default.nix-      --replace "marshmallow-sqlalchemy>=0.22.0, <0.27.0" "marshmallow-sqlalchemy" \
pkgs/development/python-modules/flask-appbuilder/default.nix-      --replace "prison>=0.2.1, <1.0.0" "prison"
pkgs/development/python-modules/flask-appbuilder/default.nix-  '';
pkgs/development/python-modules/flask-appbuilder/default.nix-
pkgs/development/python-modules/flask-appbuilder/default.nix-  # Majority of tests require network access or mongo
pkgs/development/python-modules/flask-appbuilder/default.nix-  doCheck = false;
pkgs/development/python-modules/flask-appbuilder/default.nix-
--
pkgs/development/python-modules/adb-enhanced/default.nix-  };
pkgs/development/python-modules/adb-enhanced/default.nix-
pkgs/development/python-modules/adb-enhanced/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/adb-enhanced/default.nix-
--
pkgs/development/python-modules/py3langid/default.nix-  nativeBuildInputs = [ setuptools ];
pkgs/development/python-modules/py3langid/default.nix-
pkgs/development/python-modules/py3langid/default.nix-  propagatedBuildInputs = [ numpy ];
pkgs/development/python-modules/py3langid/default.nix-
pkgs/development/python-modules/py3langid/default.nix-  nativeCheckInputs = [ pytestCheckHook ];
pkgs/development/python-modules/py3langid/default.nix-
pkgs/development/python-modules/py3langid/default.nix-  # nixify path to the courlan binary in the test suite
pkgs/development/python-modules/py3langid/default.nix-  postPatch = ''
pkgs/development/python-modules/py3langid/default.nix:    substituteInPlace tests/test_langid.py --replace "'langid'" "'$out/bin/langid'"
pkgs/development/python-modules/py3langid/default.nix:    substituteInPlace pyproject.toml --replace-fail \
pkgs/development/python-modules/py3langid/default.nix-      'numpy >= 2.0.0' numpy
pkgs/development/python-modules/py3langid/default.nix-  '';
pkgs/development/python-modules/py3langid/default.nix-
pkgs/development/python-modules/py3langid/default.nix-  pythonImportsCheck = [ "py3langid" ];
pkgs/development/python-modules/py3langid/default.nix-
pkgs/development/python-modules/py3langid/default.nix-  meta = with lib; {
pkgs/development/python-modules/py3langid/default.nix-    description = "Fork of the language identification tool langid.py, featuring a modernized codebase and faster execution times";
pkgs/development/python-modules/py3langid/default.nix-    mainProgram = "langid";
pkgs/development/python-modules/py3langid/default.nix-    homepage = "https://github.com/adbar/py3langid";
pkgs/development/python-modules/py3langid/default.nix-    changelog = "https://github.com/adbar/py3langid/blob/v${version}/HISTORY.rst";
--
--
pkgs/development/python-modules/kivy/default.nix-      name = "0001-kivy-Remove-old-Python-2-long.patch";
pkgs/development/python-modules/kivy/default.nix-      url = "https://github.com/kivy/kivy/commit/5a1b27d7d3bdee6cedb55440bfae9c4e66fb3c68.patch";
pkgs/development/python-modules/kivy/default.nix-      hash = "sha256-GDNYL8dC1Rh4KJ8oPiIjegOJGzRQ1CsgWQeAvx9+Rc8=";
pkgs/development/python-modules/kivy/default.nix-    })
pkgs/development/python-modules/kivy/default.nix-  ];
pkgs/development/python-modules/kivy/default.nix-
pkgs/development/python-modules/kivy/default.nix-  postPatch = ''
pkgs/development/python-modules/kivy/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/kivy/default.nix-      --replace-fail "setuptools~=69.2.0" "setuptools" \
pkgs/development/python-modules/kivy/default.nix-      --replace-fail "wheel~=0.44.0" "wheel" \
pkgs/development/python-modules/kivy/default.nix-      --replace-fail "cython>=0.29.1,<=3.0.11" "cython" \
pkgs/development/python-modules/kivy/default.nix-      --replace-fail "packaging~=24.0" packaging
pkgs/development/python-modules/kivy/default.nix-  ''
pkgs/development/python-modules/kivy/default.nix-  + lib.optionalString stdenv.hostPlatform.isLinux ''
pkgs/development/python-modules/kivy/default.nix:    substituteInPlace kivy/lib/mtdev.py \
pkgs/development/python-modules/kivy/default.nix-      --replace-fail "LoadLibrary('libmtdev.so.1')" "LoadLibrary('${lib.getLib mtdev}/lib/libmtdev.so.1')"
pkgs/development/python-modules/kivy/default.nix-  '';
pkgs/development/python-modules/kivy/default.nix-
pkgs/development/python-modules/kivy/default.nix-  build-system = [
pkgs/development/python-modules/kivy/default.nix-    setuptools
pkgs/development/python-modules/kivy/default.nix-    cython
--
pkgs/development/python-modules/pykrige/default.nix-
pkgs/development/python-modules/pykrige/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/pykrige/default.nix-    owner = "GeoStat-Framework";
pkgs/development/python-modules/pykrige/default.nix-    repo = "PyKrige";
pkgs/development/python-modules/pykrige/default.nix-    tag = "v${version}";
pkgs/development/python-modules/pykrige/default.nix-    hash = "sha256-9f8SNlt4qiTlXgx2ica9Y8rmnYzQ5VarvFRfoZ9bSsY=";
pkgs/development/python-modules/pykrige/default.nix-  };
pkgs/development/python-modules/pykrige/default.nix-
pkgs/development/python-modules/pykrige/default.nix-  postPatch = ''
pkgs/development/python-modules/pykrige/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/pykrige/default.nix-      --replace-fail "numpy>=2.0.0rc1,<2.3; python_version >= '3.9'" "numpy>=2.0.0";
pkgs/development/python-modules/pykrige/default.nix-  '';
pkgs/development/python-modules/pykrige/default.nix-
pkgs/development/python-modules/pykrige/default.nix-  build-system = [
pkgs/development/python-modules/pykrige/default.nix-    cython
pkgs/development/python-modules/pykrige/default.nix-    numpy
pkgs/development/python-modules/pykrige/default.nix-    scipy
pkgs/development/python-modules/pykrige/default.nix-    setuptools
pkgs/development/python-modules/pykrige/default.nix-    setuptools-scm
pkgs/development/python-modules/pykrige/default.nix-  ];
--
--
pkgs/development/python-modules/crossandra/default.nix-  build-system = [
pkgs/development/python-modules/crossandra/default.nix-    setuptools
pkgs/development/python-modules/crossandra/default.nix-    mypy
pkgs/development/python-modules/crossandra/default.nix-  ];
pkgs/development/python-modules/crossandra/default.nix-  dependencies = [ result ];
pkgs/development/python-modules/crossandra/default.nix-
pkgs/development/python-modules/crossandra/default.nix-  pythonImportsCheck = [ "crossandra" ];
pkgs/development/python-modules/crossandra/default.nix-  prePatch = ''
pkgs/development/python-modules/crossandra/default.nix-    # pythonRelaxDepsHook did not work
pkgs/development/python-modules/crossandra/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/crossandra/default.nix-      --replace-fail "result ~= 0.9.0" "result >= 0.9.0"
pkgs/development/python-modules/crossandra/default.nix-  '';
pkgs/development/python-modules/crossandra/default.nix-
pkgs/development/python-modules/crossandra/default.nix-  meta = {
pkgs/development/python-modules/crossandra/default.nix-    changelog = "https://github.com/trag1c/crossandra/blob/${src.rev}/CHANGELOG.md";
pkgs/development/python-modules/crossandra/default.nix-    description = "Fast and simple enum/regex-based tokenizer with decent configurability";
pkgs/development/python-modules/crossandra/default.nix-    license = lib.licenses.mit;
pkgs/development/python-modules/crossandra/default.nix-    homepage = "https://trag1c.github.io/crossandra";
pkgs/development/python-modules/crossandra/default.nix-    maintainers = with lib.maintainers; [ sigmanificient ];
pkgs/development/python-modules/crossandra/default.nix-  };
--
--
pkgs/development/python-modules/tskit/default.nix-  disabled = pythonOlder "3.7";
pkgs/development/python-modules/tskit/default.nix-
pkgs/development/python-modules/tskit/default.nix-  src = fetchPypi {
pkgs/development/python-modules/tskit/default.nix-    inherit pname version;
pkgs/development/python-modules/tskit/default.nix-    hash = "sha256-vawbt+OuPR9WLsGRtdhAFW4ILdKtxq98QbFwxPsb55I=";
pkgs/development/python-modules/tskit/default.nix-  };
pkgs/development/python-modules/tskit/default.nix-
pkgs/development/python-modules/tskit/default.nix-  postPatch = ''
pkgs/development/python-modules/tskit/default.nix-    # build-time constriant, used to ensure forward and backward compat
pkgs/development/python-modules/tskit/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/tskit/default.nix-      --replace-fail "numpy>=2.0" "numpy"
pkgs/development/python-modules/tskit/default.nix-  '';
pkgs/development/python-modules/tskit/default.nix-
pkgs/development/python-modules/tskit/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/tskit/default.nix-
pkgs/development/python-modules/tskit/default.nix-  dependencies = [
pkgs/development/python-modules/tskit/default.nix-    jsonschema
pkgs/development/python-modules/tskit/default.nix-    numpy
pkgs/development/python-modules/tskit/default.nix-    svgwrite
pkgs/development/python-modules/tskit/default.nix-  ];
--
--
pkgs/development/python-modules/python-xapp/default.nix-
pkgs/development/python-modules/python-xapp/default.nix-  passthru = {
pkgs/development/python-modules/python-xapp/default.nix-    updateScript = gitUpdater { ignoredVersions = "^master.*"; };
pkgs/development/python-modules/python-xapp/default.nix-    skipBulkUpdate = true; # This should be bumped as part of Cinnamon update.
pkgs/development/python-modules/python-xapp/default.nix-  };
--
pkgs/development/python-modules/cassandra-driver/default.nix-  # Make /etc/protocols accessible to allow socket.getprotobyname('tcp') in sandbox,
pkgs/development/python-modules/cassandra-driver/default.nix-  # also /etc/resolv.conf is referenced by some tests
pkgs/development/python-modules/cassandra-driver/default.nix-  preCheck =
pkgs/development/python-modules/cassandra-driver/default.nix-    (lib.optionalString stdenv.hostPlatform.isLinux ''
pkgs/development/python-modules/cassandra-driver/default.nix-      echo "nameserver 127.0.0.1" > resolv.conf
pkgs/development/python-modules/cassandra-driver/default.nix-      export NIX_REDIRECTS=/etc/protocols=${iana-etc}/etc/protocols:/etc/resolv.conf=$(realpath resolv.conf)
pkgs/development/python-modules/cassandra-driver/default.nix-      export LD_PRELOAD=${libredirect}/lib/libredirect.so
pkgs/development/python-modules/cassandra-driver/default.nix-    '')
pkgs/development/python-modules/cassandra-driver/default.nix-    + ''
pkgs/development/python-modules/cassandra-driver/default.nix-      # increase tolerance for time-based test
pkgs/development/python-modules/cassandra-driver/default.nix:      substituteInPlace tests/unit/io/utils.py --replace 'delta=.15' 'delta=.3'
pkgs/development/python-modules/cassandra-driver/default.nix-
pkgs/development/python-modules/cassandra-driver/default.nix-      export HOME=$(mktemp -d)
pkgs/development/python-modules/cassandra-driver/default.nix-      # cythonize this before we hide the source dir as it references
pkgs/development/python-modules/cassandra-driver/default.nix-      # one of its files
--
pkgs/development/python-modules/corsair-scan/default.nix-    requests
pkgs/development/python-modules/corsair-scan/default.nix-    urllib3
pkgs/development/python-modules/corsair-scan/default.nix-    tldextract
pkgs/development/python-modules/corsair-scan/default.nix-    click
pkgs/development/python-modules/corsair-scan/default.nix-  ];
--
pkgs/development/python-modules/mmcv/default.nix-    hash = "sha256-NNF9sLJWV1q6uBE73LUW4UWwYm4TBMTBJjJkFArBmsc=";
pkgs/development/python-modules/mmcv/default.nix-  };
pkgs/development/python-modules/mmcv/default.nix-
pkgs/development/python-modules/mmcv/default.nix-  postPatch =
pkgs/development/python-modules/mmcv/default.nix-    # Fails in python >= 3.13
pkgs/development/python-modules/mmcv/default.nix-    # exec(compile(f.read(), version_file, "exec")) does not populate the locals() namesp
pkgs/development/python-modules/mmcv/default.nix-    # In python 3.13, the locals() dictionary in a function does not automatically update with
pkgs/development/python-modules/mmcv/default.nix-    # changes made by exec().
pkgs/development/python-modules/mmcv/default.nix-    # https://peps.python.org/pep-0558/
pkgs/development/python-modules/mmcv/default.nix-    ''
pkgs/development/python-modules/mmcv/default.nix:      substituteInPlace setup.py \
pkgs/development/python-modules/mmcv/default.nix-        --replace-fail "cpu_use = 4" "cpu_use = $NIX_BUILD_CORES" \
pkgs/development/python-modules/mmcv/default.nix-        --replace-fail "return locals()['__version__']" "return '${version}'"
pkgs/development/python-modules/mmcv/default.nix-    '';
pkgs/development/python-modules/mmcv/default.nix-
--
pkgs/development/python-modules/dissect-target/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/dissect-target/default.nix-    owner = "fox-it";
pkgs/development/python-modules/dissect-target/default.nix-    repo = "dissect.target";
pkgs/development/python-modules/dissect-target/default.nix-    tag = version;
pkgs/development/python-modules/dissect-target/default.nix-    hash = "sha256-N7GxaXQj7mrTOsNGek4ZZlVF9GH/rm5CFKpYFMLJw8k=";
pkgs/development/python-modules/dissect-target/default.nix-    fetchLFS = true;
pkgs/development/python-modules/dissect-target/default.nix-  };
pkgs/development/python-modules/dissect-target/default.nix-
pkgs/development/python-modules/dissect-target/default.nix-  postPatch = ''
pkgs/development/python-modules/dissect-target/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/dissect-target/default.nix-      --replace-fail "flow.record~=" "flow.record>="
pkgs/development/python-modules/dissect-target/default.nix-  '';
pkgs/development/python-modules/dissect-target/default.nix-
pkgs/development/python-modules/dissect-target/default.nix-  build-system = [
pkgs/development/python-modules/dissect-target/default.nix-    setuptools
pkgs/development/python-modules/dissect-target/default.nix-    setuptools-scm
pkgs/development/python-modules/dissect-target/default.nix-  ];
pkgs/development/python-modules/dissect-target/default.nix-
pkgs/development/python-modules/dissect-target/default.nix-  dependencies = [
pkgs/development/python-modules/dissect-target/default.nix-    defusedxml
--
--
pkgs/development/python-modules/finetuning-scheduler/default.nix-
pkgs/development/python-modules/finetuning-scheduler/default.nix-  patches = [
pkgs/development/python-modules/finetuning-scheduler/default.nix-    (fetchpatch {
pkgs/development/python-modules/finetuning-scheduler/default.nix-      url = "https://github.com/speediedan/finetuning-scheduler/commit/78e6e225f353d1ba95db05d7fc6ff541859ed6a2.patch";
pkgs/development/python-modules/finetuning-scheduler/default.nix-      hash = "sha256-7mbtsaHrnHph8lvuwhBGqxPQimbZcbGeyBYXzApFPn4=";
pkgs/development/python-modules/finetuning-scheduler/default.nix-    })
pkgs/development/python-modules/finetuning-scheduler/default.nix-  ];
pkgs/development/python-modules/finetuning-scheduler/default.nix-
pkgs/development/python-modules/finetuning-scheduler/default.nix-  postPatch = ''
pkgs/development/python-modules/finetuning-scheduler/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/finetuning-scheduler/default.nix-      --replace-fail "setuptools<77.0.0" "setuptools"
pkgs/development/python-modules/finetuning-scheduler/default.nix-  '';
pkgs/development/python-modules/finetuning-scheduler/default.nix-
pkgs/development/python-modules/finetuning-scheduler/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/finetuning-scheduler/default.nix-
pkgs/development/python-modules/finetuning-scheduler/default.nix-  pythonRelaxDeps = [
pkgs/development/python-modules/finetuning-scheduler/default.nix-    "pytorch-lightning"
pkgs/development/python-modules/finetuning-scheduler/default.nix-  ];
pkgs/development/python-modules/finetuning-scheduler/default.nix-
pkgs/development/python-modules/finetuning-scheduler/default.nix-  dependencies = [
--
--
pkgs/development/python-modules/glyphsets/default.nix-
pkgs/development/python-modules/glyphsets/default.nix-  disabled = pythonOlder "3.8";
pkgs/development/python-modules/glyphsets/default.nix-
pkgs/development/python-modules/glyphsets/default.nix-  src = fetchPypi {
pkgs/development/python-modules/glyphsets/default.nix-    inherit pname version;
pkgs/development/python-modules/glyphsets/default.nix-    hash = "sha256-jza6VQ3PZAQPku2hyo0KeO59r64Q9TpqLCI0dIX/URU=";
pkgs/development/python-modules/glyphsets/default.nix-  };
pkgs/development/python-modules/glyphsets/default.nix-
pkgs/development/python-modules/glyphsets/default.nix-  postPatch = ''
pkgs/development/python-modules/glyphsets/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/glyphsets/default.nix-      --replace-fail "setuptools_scm>=8.1.0,<8.2" setuptools_scm
pkgs/development/python-modules/glyphsets/default.nix-  '';
pkgs/development/python-modules/glyphsets/default.nix-
pkgs/development/python-modules/glyphsets/default.nix-  env.PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION = "python";
pkgs/development/python-modules/glyphsets/default.nix-
pkgs/development/python-modules/glyphsets/default.nix-  build-system = [
pkgs/development/python-modules/glyphsets/default.nix-    setuptools
pkgs/development/python-modules/glyphsets/default.nix-    setuptools-scm
pkgs/development/python-modules/glyphsets/default.nix-  ];
pkgs/development/python-modules/glyphsets/default.nix-
--
--
pkgs/development/python-modules/reproject/default.nix-
pkgs/development/python-modules/reproject/default.nix-  disabled = pythonOlder "3.10";
pkgs/development/python-modules/reproject/default.nix-
pkgs/development/python-modules/reproject/default.nix-  src = fetchPypi {
pkgs/development/python-modules/reproject/default.nix-    inherit pname version;
pkgs/development/python-modules/reproject/default.nix-    hash = "sha256-l9pmxtXIGnl8T8fCsUp/5y3kReg3MXdaN0i2rpcEqE4=";
pkgs/development/python-modules/reproject/default.nix-  };
pkgs/development/python-modules/reproject/default.nix-
pkgs/development/python-modules/reproject/default.nix-  postPatch = ''
pkgs/development/python-modules/reproject/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/reproject/default.nix-      --replace "cython==" "cython>="
pkgs/development/python-modules/reproject/default.nix-  '';
pkgs/development/python-modules/reproject/default.nix-
pkgs/development/python-modules/reproject/default.nix-  nativeBuildInputs = [
pkgs/development/python-modules/reproject/default.nix-    astropy-extension-helpers
pkgs/development/python-modules/reproject/default.nix-    cython
pkgs/development/python-modules/reproject/default.nix-    numpy
pkgs/development/python-modules/reproject/default.nix-    setuptools-scm
pkgs/development/python-modules/reproject/default.nix-  ];
pkgs/development/python-modules/reproject/default.nix-
--
--
pkgs/development/python-modules/groq/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/groq/default.nix-    owner = "groq";
pkgs/development/python-modules/groq/default.nix-    repo = "groq-python";
pkgs/development/python-modules/groq/default.nix-    tag = "v${version}";
pkgs/development/python-modules/groq/default.nix-    hash = "sha256-6oTRqAt421WE0s5e2kqDtCgOLg1bSqTTQldQ5D05Flo=";
pkgs/development/python-modules/groq/default.nix-  };
pkgs/development/python-modules/groq/default.nix-
pkgs/development/python-modules/groq/default.nix-  postPatch = ''
pkgs/development/python-modules/groq/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/groq/default.nix-      --replace-fail "hatchling==1.26.3" \
pkgs/development/python-modules/groq/default.nix-      "hatchling>=1.26.3"
pkgs/development/python-modules/groq/default.nix-  '';
pkgs/development/python-modules/groq/default.nix-
pkgs/development/python-modules/groq/default.nix-  build-system = [
pkgs/development/python-modules/groq/default.nix-    hatch-fancy-pypi-readme
pkgs/development/python-modules/groq/default.nix-    hatchling
pkgs/development/python-modules/groq/default.nix-  ];
pkgs/development/python-modules/groq/default.nix-
pkgs/development/python-modules/groq/default.nix-  dependencies = [
--
pkgs/development/python-modules/systembridgemodels/default.nix-  disabled = pythonOlder "3.11";
pkgs/development/python-modules/systembridgemodels/default.nix-
pkgs/development/python-modules/systembridgemodels/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/systembridgemodels/default.nix-    owner = "timmo001";
pkgs/development/python-modules/systembridgemodels/default.nix-    repo = "system-bridge-models";
pkgs/development/python-modules/systembridgemodels/default.nix-    tag = version;
pkgs/development/python-modules/systembridgemodels/default.nix-    hash = "sha256-FjHDd7nI30ChaClL0b1ME9Zv+DV0BiMsfgGOKQF/qBk=";
pkgs/development/python-modules/systembridgemodels/default.nix-  };
pkgs/development/python-modules/systembridgemodels/default.nix-
pkgs/development/python-modules/systembridgemodels/default.nix-  postPatch = ''
pkgs/development/python-modules/systembridgemodels/default.nix:    substituteInPlace requirements_setup.txt \
pkgs/development/python-modules/systembridgemodels/default.nix-      --replace-fail ">=" " #"
pkgs/development/python-modules/systembridgemodels/default.nix-
pkgs/development/python-modules/systembridgemodels/default.nix:    substituteInPlace systembridgemodels/_version.py \
pkgs/development/python-modules/systembridgemodels/default.nix-      --replace-fail ", dev=0" ""
pkgs/development/python-modules/systembridgemodels/default.nix-  '';
pkgs/development/python-modules/systembridgemodels/default.nix-
pkgs/development/python-modules/systembridgemodels/default.nix-  build-system = [
pkgs/development/python-modules/systembridgemodels/default.nix-    incremental
pkgs/development/python-modules/systembridgemodels/default.nix-    setuptools
pkgs/development/python-modules/systembridgemodels/default.nix-  ];
pkgs/development/python-modules/systembridgemodels/default.nix-
--
pkgs/development/python-modules/pypiserver/default.nix-
pkgs/development/python-modules/pypiserver/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/pypiserver/default.nix-    owner = "pypiserver";
pkgs/development/python-modules/pypiserver/default.nix-    repo = "pypiserver";
pkgs/development/python-modules/pypiserver/default.nix-    tag = "v${version}";
pkgs/development/python-modules/pypiserver/default.nix-    hash = "sha256-ODwDYAEAqel31+kR/BE1yBfgOZOtPz3iaCLg/d6jbb4=";
pkgs/development/python-modules/pypiserver/default.nix-  };
pkgs/development/python-modules/pypiserver/default.nix-
pkgs/development/python-modules/pypiserver/default.nix-  postPatch = ''
pkgs/development/python-modules/pypiserver/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/pypiserver/default.nix-      --replace-fail '"setuptools-git>=0.3",' ""
pkgs/development/python-modules/pypiserver/default.nix-  '';
pkgs/development/python-modules/pypiserver/default.nix-
pkgs/development/python-modules/pypiserver/default.nix-  build-system = [
pkgs/development/python-modules/pypiserver/default.nix-    setuptools
pkgs/development/python-modules/pypiserver/default.nix-  ];
pkgs/development/python-modules/pypiserver/default.nix-
pkgs/development/python-modules/pypiserver/default.nix-  dependencies = [
pkgs/development/python-modules/pypiserver/default.nix-    distutils
pkgs/development/python-modules/pypiserver/default.nix-    pip
--
--
pkgs/development/python-modules/dynalite-panel/default.nix-  version = "0.0.4";
pkgs/development/python-modules/dynalite-panel/default.nix-  pyproject = true;
pkgs/development/python-modules/dynalite-panel/default.nix-
pkgs/development/python-modules/dynalite-panel/default.nix-  src = fetchPypi {
pkgs/development/python-modules/dynalite-panel/default.nix-    inherit pname version;
pkgs/development/python-modules/dynalite-panel/default.nix-    hash = "sha256-m7nQzbxRe2qXUWAMeQlDZtc9F01DsbTzF/kI0ci3TFE=";
pkgs/development/python-modules/dynalite-panel/default.nix-  };
pkgs/development/python-modules/dynalite-panel/default.nix-
pkgs/development/python-modules/dynalite-panel/default.nix-  postPatch = ''
pkgs/development/python-modules/dynalite-panel/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/dynalite-panel/default.nix-      --replace "~=" ">="
pkgs/development/python-modules/dynalite-panel/default.nix-  '';
pkgs/development/python-modules/dynalite-panel/default.nix-
pkgs/development/python-modules/dynalite-panel/default.nix-  nativeBuildInputs = [ setuptools ];
pkgs/development/python-modules/dynalite-panel/default.nix-
pkgs/development/python-modules/dynalite-panel/default.nix-  pythonImportsCheck = [ "dynalite_panel" ];
pkgs/development/python-modules/dynalite-panel/default.nix-
pkgs/development/python-modules/dynalite-panel/default.nix-  # upstream has no tests
pkgs/development/python-modules/dynalite-panel/default.nix-  doCheck = false;
pkgs/development/python-modules/dynalite-panel/default.nix-
--
--
pkgs/development/python-modules/limits/default.nix-  ];
pkgs/development/python-modules/limits/default.nix-
pkgs/development/python-modules/limits/default.nix-  postPatch = ''
pkgs/development/python-modules/limits/default.nix:    substituteInPlace pytest.ini \
pkgs/development/python-modules/limits/default.nix-      --replace-fail "-K" ""
pkgs/development/python-modules/limits/default.nix-
pkgs/development/python-modules/limits/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/limits/default.nix-      --replace-fail "versioneer.get_version()" "'${version}'"
pkgs/development/python-modules/limits/default.nix-
pkgs/development/python-modules/limits/default.nix-    # Recreate _version.py, deleted at fetch time due to non-reproducibility.
pkgs/development/python-modules/limits/default.nix-    echo 'def get_versions(): return {"version": "${version}"}' > limits/_version.py
pkgs/development/python-modules/limits/default.nix-  '';
pkgs/development/python-modules/limits/default.nix-
pkgs/development/python-modules/limits/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/limits/default.nix-
pkgs/development/python-modules/limits/default.nix-  dependencies = [
pkgs/development/python-modules/limits/default.nix-    deprecated
--
pkgs/development/python-modules/speechrecognition/default.nix-    repo = "speech_recognition";
pkgs/development/python-modules/speechrecognition/default.nix-    tag = version;
pkgs/development/python-modules/speechrecognition/default.nix-    hash = "sha256-g//KKxPRe1pWVJo7GsRNIV59r0J7XJEoXvH0tGuV3Jk=";
--
pkgs/development/python-modules/ismartgate/default.nix-
pkgs/development/python-modules/ismartgate/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/ismartgate/default.nix-    owner = "bdraco";
pkgs/development/python-modules/ismartgate/default.nix-    repo = "ismartgate";
pkgs/development/python-modules/ismartgate/default.nix-    tag = "v${version}";
pkgs/development/python-modules/ismartgate/default.nix-    hash = "sha256-8c05zzDav87gTL2CI7Aoi6ALwLw76H9xj+90xH31hdE=";
pkgs/development/python-modules/ismartgate/default.nix-  };
pkgs/development/python-modules/ismartgate/default.nix-
pkgs/development/python-modules/ismartgate/default.nix-  postPatch = ''
pkgs/development/python-modules/ismartgate/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/ismartgate/default.nix-      --replace '"pytest-runner>=5.2",' ""
pkgs/development/python-modules/ismartgate/default.nix-  '';
pkgs/development/python-modules/ismartgate/default.nix-
pkgs/development/python-modules/ismartgate/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/ismartgate/default.nix-    click
pkgs/development/python-modules/ismartgate/default.nix-    defusedxml
pkgs/development/python-modules/ismartgate/default.nix-    dicttoxml
pkgs/development/python-modules/ismartgate/default.nix-    httpx
pkgs/development/python-modules/ismartgate/default.nix-    pycryptodome
pkgs/development/python-modules/ismartgate/default.nix-    typing-extensions
--
--
--
pkgs/development/python-modules/mxnet/default.nix-
pkgs/development/python-modules/mxnet/default.nix-  pythonRelaxDeps = [
pkgs/development/python-modules/mxnet/default.nix-    "graphviz"
pkgs/development/python-modules/mxnet/default.nix-    "numpy"
pkgs/development/python-modules/mxnet/default.nix-  ];
pkgs/development/python-modules/mxnet/default.nix-
pkgs/development/python-modules/mxnet/default.nix-  LD_LIBRARY_PATH = lib.makeLibraryPath [ pkgs.mxnet ];
pkgs/development/python-modules/mxnet/default.nix-
pkgs/development/python-modules/mxnet/default.nix-  postPatch = ''
pkgs/development/python-modules/mxnet/default.nix-    # Required to support numpy >=1.24 where np.bool is removed in favor of just bool
pkgs/development/python-modules/mxnet/default.nix:    substituteInPlace python/mxnet/numpy/utils.py \
pkgs/development/python-modules/mxnet/default.nix-      --replace-fail "bool = onp.bool" "bool = bool"
pkgs/development/python-modules/mxnet/default.nix-  '';
pkgs/development/python-modules/mxnet/default.nix-
pkgs/development/python-modules/mxnet/default.nix-  preConfigure = ''
pkgs/development/python-modules/mxnet/default.nix-    cd python
pkgs/development/python-modules/mxnet/default.nix-  '';
pkgs/development/python-modules/mxnet/default.nix-
pkgs/development/python-modules/mxnet/default.nix-  postInstall = ''
pkgs/development/python-modules/mxnet/default.nix-    rm -rf $out/mxnet
--
pkgs/development/python-modules/pysnooz/default.nix-    hash = "sha256-jOXmaJprU35sdNRrBBx/YUyiDyyaE1qodWksXkTSEe0=";
pkgs/development/python-modules/pysnooz/default.nix-  };
pkgs/development/python-modules/pysnooz/default.nix-
pkgs/development/python-modules/pysnooz/default.nix-  patches = [
pkgs/development/python-modules/pysnooz/default.nix-    # https://github.com/AustinBrunkhorst/pysnooz/pull/20
pkgs/development/python-modules/pysnooz/default.nix-    ./bleak-compat.patch
pkgs/development/python-modules/pysnooz/default.nix-  ];
pkgs/development/python-modules/pysnooz/default.nix-
pkgs/development/python-modules/pysnooz/default.nix-  postPatch = ''
pkgs/development/python-modules/pysnooz/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/pysnooz/default.nix-      --replace-fail 'transitions = "^0.8.11"' 'transitions = ">=0.8.11"' \
pkgs/development/python-modules/pysnooz/default.nix-      --replace-fail 'Events = "^0.4"' 'Events = ">=0.4"'
pkgs/development/python-modules/pysnooz/default.nix-  '';
pkgs/development/python-modules/pysnooz/default.nix-
pkgs/development/python-modules/pysnooz/default.nix-  build-system = [ poetry-core ];
pkgs/development/python-modules/pysnooz/default.nix-
pkgs/development/python-modules/pysnooz/default.nix-  dependencies = [
pkgs/development/python-modules/pysnooz/default.nix-    bleak
pkgs/development/python-modules/pysnooz/default.nix-    bleak-retry-connector
pkgs/development/python-modules/pysnooz/default.nix-    bluetooth-sensor-state-data
--
pkgs/development/python-modules/aiogithubapi/default.nix-    hash = "sha256-zl9QpFpkvSTs0BUDMBmwTeLY1YvNRSqbkIZ5LDUP3zw=";
--
pkgs/development/python-modules/datatable/default.nix-    hash = "sha256-lEXQwhx2msnJkkRrTkAwYttlYTISyH/Z7dSalqRrOhI=";
pkgs/development/python-modules/datatable/default.nix-  };
pkgs/development/python-modules/datatable/default.nix-
pkgs/development/python-modules/datatable/default.nix-  postPatch = ''
pkgs/development/python-modules/datatable/default.nix-    # tarball doesn't appear to have been shipped totally ready-to-build
pkgs/development/python-modules/datatable/default.nix:    substituteInPlace ci/ext.py \
pkgs/development/python-modules/datatable/default.nix-      --replace \
pkgs/development/python-modules/datatable/default.nix-        'shell_cmd(["git"' \
pkgs/development/python-modules/datatable/default.nix-        '"0000000000000000000000000000000000000000" or shell_cmd(["git"'
pkgs/development/python-modules/datatable/default.nix-    # TODO revert back to use ${version} when bumping to the next stable release
pkgs/development/python-modules/datatable/default.nix-    echo '1.0' > VERSION.txt
pkgs/development/python-modules/datatable/default.nix-
pkgs/development/python-modules/datatable/default.nix-    # don't make assumptions about architecture
pkgs/development/python-modules/datatable/default.nix-    sed -i '/-m64/d' ci/ext.py
pkgs/development/python-modules/datatable/default.nix-  '';
pkgs/development/python-modules/datatable/default.nix-  DT_RELEASE = "1";
--
pkgs/development/python-modules/dlib/default.nix-  format = "setuptools";
pkgs/development/python-modules/dlib/default.nix-
pkgs/development/python-modules/dlib/default.nix-  patches = [ ./build-cores.patch ];
pkgs/development/python-modules/dlib/default.nix-
pkgs/development/python-modules/dlib/default.nix-  nativeCheckInputs = [
pkgs/development/python-modules/dlib/default.nix-    pytestCheckHook
pkgs/development/python-modules/dlib/default.nix-    more-itertools
pkgs/development/python-modules/dlib/default.nix-  ];
pkgs/development/python-modules/dlib/default.nix-
pkgs/development/python-modules/dlib/default.nix-  postPatch = ''
pkgs/development/python-modules/dlib/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/dlib/default.nix-      --replace "more-itertools<6.0.0" "more-itertools" \
pkgs/development/python-modules/dlib/default.nix-      --replace "pytest==3.8" "pytest"
pkgs/development/python-modules/dlib/default.nix-  '';
pkgs/development/python-modules/dlib/default.nix-
pkgs/development/python-modules/dlib/default.nix-  # Pass CMake flags through to the build script
pkgs/development/python-modules/dlib/default.nix-  preConfigure = ''
pkgs/development/python-modules/dlib/default.nix-    for flag in $cmakeFlags; do
pkgs/development/python-modules/dlib/default.nix-      if [[ "$flag" == -D* ]]; then
pkgs/development/python-modules/dlib/default.nix-        setupPyBuildFlags+=" --set ''${flag#-D}"
pkgs/development/python-modules/dlib/default.nix-      fi
--
--
pkgs/development/python-modules/boltztrap2/default.nix-  disabled = pythonOlder "3.5";
pkgs/development/python-modules/boltztrap2/default.nix-
pkgs/development/python-modules/boltztrap2/default.nix-  src = fetchPypi {
pkgs/development/python-modules/boltztrap2/default.nix-    pname = "boltztrap2";
pkgs/development/python-modules/boltztrap2/default.nix-    inherit version;
pkgs/development/python-modules/boltztrap2/default.nix-    hash = "sha256-JUIGh/6AF+xYLmF3QN47/A5E9zPKdhO2lhn97giZJ48=";
pkgs/development/python-modules/boltztrap2/default.nix-  };
pkgs/development/python-modules/boltztrap2/default.nix-
pkgs/development/python-modules/boltztrap2/default.nix-  postPatch = ''
pkgs/development/python-modules/boltztrap2/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/boltztrap2/default.nix-      --replace-fail "numpy>=2.0.0" "numpy"
pkgs/development/python-modules/boltztrap2/default.nix-  '';
pkgs/development/python-modules/boltztrap2/default.nix-
pkgs/development/python-modules/boltztrap2/default.nix-  dontUseCmakeConfigure = true;
pkgs/development/python-modules/boltztrap2/default.nix-
pkgs/development/python-modules/boltztrap2/default.nix-  nativeBuildInputs = [
pkgs/development/python-modules/boltztrap2/default.nix-    cmake
pkgs/development/python-modules/boltztrap2/default.nix-    cython
pkgs/development/python-modules/boltztrap2/default.nix-  ];
pkgs/development/python-modules/boltztrap2/default.nix-
--
--
pkgs/development/python-modules/devtools/default.nix-    hash = "sha256-1HFbNswdKa/9cQX0Gf6lLW1V5Kt/N4X6/5kQDdzp1Wo=";
pkgs/development/python-modules/devtools/default.nix-  };
pkgs/development/python-modules/devtools/default.nix-
pkgs/development/python-modules/devtools/default.nix-  patches = [
pkgs/development/python-modules/devtools/default.nix-    # https://github.com/samuelcolvin/python-devtools/pull/166
pkgs/development/python-modules/devtools/default.nix-    ./fix-test-ast-expr.patch
pkgs/development/python-modules/devtools/default.nix-  ];
pkgs/development/python-modules/devtools/default.nix-
pkgs/development/python-modules/devtools/default.nix-  postPatch = ''
pkgs/development/python-modules/devtools/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/devtools/default.nix-      --replace-fail 'asttokens>=2.0.0,<3.0.0' 'asttokens>=2.0.0' \
pkgs/development/python-modules/devtools/default.nix-  '';
pkgs/development/python-modules/devtools/default.nix-
pkgs/development/python-modules/devtools/default.nix-  build-system = [ hatchling ];
pkgs/development/python-modules/devtools/default.nix-
pkgs/development/python-modules/devtools/default.nix-  dependencies = [
pkgs/development/python-modules/devtools/default.nix-    asttokens
pkgs/development/python-modules/devtools/default.nix-    executing
pkgs/development/python-modules/devtools/default.nix-    pygments
pkgs/development/python-modules/devtools/default.nix-  ];
--
--
pkgs/development/python-modules/tinygrad/default.nix-    + ''
pkgs/development/python-modules/tinygrad/default.nix:      substituteInPlace tinygrad/runtime/support/llvm.py \
pkgs/development/python-modules/tinygrad/default.nix-        --replace-fail "ctypes.util.find_library('LLVM')" "'${lib.getLib llvmPackages.llvm}/lib/libLLVM.so'"
pkgs/development/python-modules/tinygrad/default.nix-    ''
pkgs/development/python-modules/tinygrad/default.nix-    + lib.optionalString stdenv.hostPlatform.isLinux ''
pkgs/development/python-modules/tinygrad/default.nix:      substituteInPlace tinygrad/runtime/autogen/opencl.py \
pkgs/development/python-modules/tinygrad/default.nix-        --replace-fail "ctypes.util.find_library('OpenCL')" "'${ocl-icd}/lib/libOpenCL.so'"
pkgs/development/python-modules/tinygrad/default.nix-    ''
pkgs/development/python-modules/tinygrad/default.nix-    # test/test_tensor.py imports the PTX variable from the cuda_compiler.py file.
pkgs/development/python-modules/tinygrad/default.nix-    # This import leads to loading the libnvrtc.so library that is not substituted when cudaSupport = false.
pkgs/development/python-modules/tinygrad/default.nix-    # -> As a fix, we hardcode this variable to False
pkgs/development/python-modules/tinygrad/default.nix-    + lib.optionalString (!cudaSupport) ''
pkgs/development/python-modules/tinygrad/default.nix:      substituteInPlace test/test_tensor.py \
pkgs/development/python-modules/tinygrad/default.nix-        --replace-fail "from tinygrad.runtime.support.compiler_cuda import PTX" "PTX = False"
pkgs/development/python-modules/tinygrad/default.nix-    ''
pkgs/development/python-modules/tinygrad/default.nix-    # `cuda_fp16.h` and co. are needed at runtime to compile kernels
pkgs/development/python-modules/tinygrad/default.nix-    + lib.optionalString cudaSupport ''
pkgs/development/python-modules/tinygrad/default.nix:      substituteInPlace tinygrad/runtime/support/compiler_cuda.py \
pkgs/development/python-modules/tinygrad/default.nix-        --replace-fail \
pkgs/development/python-modules/tinygrad/default.nix-        ', "-I/usr/local/cuda/include", "-I/usr/include", "-I/opt/cuda/include/"' \
pkgs/development/python-modules/tinygrad/default.nix-        ', "-I${lib.getDev cudaPackages.cuda_cudart}/include/"'
--
pkgs/development/python-modules/pcodedmp/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/pcodedmp/default.nix-    owner = "bontchev";
pkgs/development/python-modules/pcodedmp/default.nix-    repo = "pcodedmp";
pkgs/development/python-modules/pcodedmp/default.nix-    rev = version;
pkgs/development/python-modules/pcodedmp/default.nix-    hash = "sha256-SYOFGMvrzxDPMACaCvqwU28Mh9LEuvFBGvAph4X+geo=";
pkgs/development/python-modules/pcodedmp/default.nix-  };
pkgs/development/python-modules/pcodedmp/default.nix-
pkgs/development/python-modules/pcodedmp/default.nix-  postPatch = ''
pkgs/development/python-modules/pcodedmp/default.nix-    # Circular dependency
pkgs/development/python-modules/pcodedmp/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/pcodedmp/default.nix-      --replace "'oletools>=0.54'," ""
pkgs/development/python-modules/pcodedmp/default.nix-  '';
pkgs/development/python-modules/pcodedmp/default.nix-
pkgs/development/python-modules/pcodedmp/default.nix-  # Module doesn't have tests
pkgs/development/python-modules/pcodedmp/default.nix-  doCheck = false;
pkgs/development/python-modules/pcodedmp/default.nix-
pkgs/development/python-modules/pcodedmp/default.nix-  pythonImportsCheck = [ "pcodedmp" ];
pkgs/development/python-modules/pcodedmp/default.nix-
pkgs/development/python-modules/pcodedmp/default.nix-  meta = with lib; {
pkgs/development/python-modules/pcodedmp/default.nix-    description = "Python VBA p-code disassembler";
--
--
pkgs/development/python-modules/pesq/default.nix-    # pythonRemoveDeps does not work for removing pytest-runner
pkgs/development/python-modules/pesq/default.nix-    ''
pkgs/development/python-modules/pesq/default.nix:      substituteInPlace setup.py \
pkgs/development/python-modules/pesq/default.nix-        --replace-fail ", 'pytest-runner'" ""
pkgs/development/python-modules/pesq/default.nix-    ''
pkgs/development/python-modules/pesq/default.nix-    # Flaky tests: numerical equality is not satisfied on ARM platforms
pkgs/development/python-modules/pesq/default.nix-    + ''
pkgs/development/python-modules/pesq/default.nix:      substituteInPlace tests/test_pesq.py \
pkgs/development/python-modules/pesq/default.nix-        --replace-fail \
pkgs/development/python-modules/pesq/default.nix-          "assert score == 1.6072081327438354" \
pkgs/development/python-modules/pesq/default.nix-          "assert abs(score - 1.6072081327438354) < 1e-5" \
pkgs/development/python-modules/pesq/default.nix-        --replace-fail \
pkgs/development/python-modules/pesq/default.nix-          "assert score == [1.6072081327438354]" \
pkgs/development/python-modules/pesq/default.nix-          "assert np.allclose(np.array(score), np.array([1.6072081327438354]))"
pkgs/development/python-modules/pesq/default.nix-    '';
pkgs/development/python-modules/pesq/default.nix-
pkgs/development/python-modules/pesq/default.nix-  build-system = [
pkgs/development/python-modules/pesq/default.nix-    cython
--
pkgs/development/python-modules/pot/default.nix-        ++ plot
pkgs/development/python-modules/pot/default.nix-      );
--
pkgs/development/python-modules/quickjs/default.nix-
pkgs/development/python-modules/quickjs/default.nix-  # Upstream uses Git submodules; let's de-vendor and use Nix, so that we gain security fixes like
pkgs/development/python-modules/quickjs/default.nix-  # https://github.com/NixOS/nixpkgs/pull/407469
pkgs/development/python-modules/quickjs/default.nix-  prePatch = ''
pkgs/development/python-modules/quickjs/default.nix-    rmdir upstream-quickjs
pkgs/development/python-modules/quickjs/default.nix-    ln -s ${srcOnly quickjs} upstream-quickjs
pkgs/development/python-modules/quickjs/default.nix-  '';
pkgs/development/python-modules/quickjs/default.nix-
pkgs/development/python-modules/quickjs/default.nix-  postPatch = ''
pkgs/development/python-modules/quickjs/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/quickjs/default.nix-      --replace-fail poetry>=1.5.0 poetry \
pkgs/development/python-modules/quickjs/default.nix-      --replace-fail poetry poetry-core \
pkgs/development/python-modules/quickjs/default.nix-      --replace-fail 'version = "0"' 'version = "${version}"'
pkgs/development/python-modules/quickjs/default.nix-  '';
pkgs/development/python-modules/quickjs/default.nix-
pkgs/development/python-modules/quickjs/default.nix-  build-system = [
pkgs/development/python-modules/quickjs/default.nix-    poetry-core
pkgs/development/python-modules/quickjs/default.nix-    setuptools
pkgs/development/python-modules/quickjs/default.nix-  ];
pkgs/development/python-modules/quickjs/default.nix-
--
--
pkgs/development/python-modules/uv/default.nix-    # Do not rely on path lookup at runtime to find the uv binary.
pkgs/development/python-modules/uv/default.nix-    # Use the propagated binary instead.
pkgs/development/python-modules/uv/default.nix-    ''
pkgs/development/python-modules/uv/default.nix:      substituteInPlace python/uv/_find_uv.py \
pkgs/development/python-modules/uv/default.nix-        --replace-fail '"""Return the uv binary path."""' "return '${lib.getExe uv}'"
pkgs/development/python-modules/uv/default.nix-    ''
pkgs/development/python-modules/uv/default.nix-    # Sidestep the maturin build system in favour of reusing the binary already built by nixpkgs,
pkgs/development/python-modules/uv/default.nix-    # to avoid rebuilding the uv binary for every active python package set.
pkgs/development/python-modules/uv/default.nix-    + ''
pkgs/development/python-modules/uv/default.nix:      substituteInPlace pyproject.toml \
pkgs/development/python-modules/uv/default.nix-        --replace-fail 'requires = ["maturin>=1.0,<2.0"]' 'requires = ["hatchling"]' \
pkgs/development/python-modules/uv/default.nix-        --replace-fail 'build-backend = "maturin"' 'build-backend = "hatchling.build"'
pkgs/development/python-modules/uv/default.nix-
pkgs/development/python-modules/uv/default.nix-      cat >> pyproject.toml <<EOF
pkgs/development/python-modules/uv/default.nix-      [tool.hatch.build]
pkgs/development/python-modules/uv/default.nix-      packages = ['python/uv']
pkgs/development/python-modules/uv/default.nix-
pkgs/development/python-modules/uv/default.nix-      EOF
pkgs/development/python-modules/uv/default.nix-    '';
pkgs/development/python-modules/uv/default.nix-
--
pkgs/development/python-modules/xml2rfc/default.nix-  disabled = pythonOlder "3.9";
pkgs/development/python-modules/xml2rfc/default.nix-
pkgs/development/python-modules/xml2rfc/default.nix-  src = fetchFromGitHub {
--
pkgs/development/python-modules/worldengine/default.nix-    noise
pkgs/development/python-modules/worldengine/default.nix-    numpy
pkgs/development/python-modules/worldengine/default.nix-    protobuf
pkgs/development/python-modules/worldengine/default.nix-    purepng
pkgs/development/python-modules/worldengine/default.nix-    pyplatec
pkgs/development/python-modules/worldengine/default.nix-    six
pkgs/development/python-modules/worldengine/default.nix-  ];
pkgs/development/python-modules/worldengine/default.nix-
pkgs/development/python-modules/worldengine/default.nix-  prePatch = ''
pkgs/development/python-modules/worldengine/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/worldengine/default.nix-      --replace pypng>=0.0.18 purepng \
pkgs/development/python-modules/worldengine/default.nix-      --replace 'numpy>=1.9.2, <= 1.10.0.post2' 'numpy' \
pkgs/development/python-modules/worldengine/default.nix-      --replace 'argparse==1.2.1' "" \
pkgs/development/python-modules/worldengine/default.nix-      --replace 'protobuf==3.0.0a3' 'protobuf' \
pkgs/development/python-modules/worldengine/default.nix-      --replace 'noise==1.2.2' 'noise' \
pkgs/development/python-modules/worldengine/default.nix-      --replace 'PyPlatec==1.4.0' 'PyPlatec' \
pkgs/development/python-modules/worldengine/default.nix-
pkgs/development/python-modules/worldengine/default.nix:    substituteInPlace \
pkgs/development/python-modules/worldengine/default.nix-      worldengine/{draw.py,hdf5_serialization.py} \
pkgs/development/python-modules/worldengine/default.nix-      --replace numpy.float float
pkgs/development/python-modules/worldengine/default.nix-  '';
pkgs/development/python-modules/worldengine/default.nix-
--
pkgs/development/python-modules/schema-salad/default.nix-    owner = "common-workflow-language";
pkgs/development/python-modules/schema-salad/default.nix-    repo = "schema_salad";
pkgs/development/python-modules/schema-salad/default.nix-    tag = version;
pkgs/development/python-modules/schema-salad/default.nix-    hash = "sha256-FEdv0VORkvXhqXPrmyCZ1Ib5Lz4fKwRkEqEcEXpfGq8=";
pkgs/development/python-modules/schema-salad/default.nix-  };
pkgs/development/python-modules/schema-salad/default.nix-
pkgs/development/python-modules/schema-salad/default.nix-  pythonRelaxDeps = [ "mistune" ];
pkgs/development/python-modules/schema-salad/default.nix-
pkgs/development/python-modules/schema-salad/default.nix-  postPatch = ''
pkgs/development/python-modules/schema-salad/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/schema-salad/default.nix-      --replace-fail 'pytest_runner + ["setuptools_scm>=8.0.4,<9"]' '["setuptools_scm"]'
pkgs/development/python-modules/schema-salad/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/schema-salad/default.nix-      --replace-fail '"setuptools_scm[toml]>=8.0.4,<9"' '"setuptools_scm[toml]"' \
pkgs/development/python-modules/schema-salad/default.nix-      --replace-fail "mypy[mypyc]==1.17.0" "mypy"
pkgs/development/python-modules/schema-salad/default.nix-    sed -i "/black>=/d" pyproject.toml
pkgs/development/python-modules/schema-salad/default.nix-  '';
pkgs/development/python-modules/schema-salad/default.nix-
pkgs/development/python-modules/schema-salad/default.nix-  build-system = [ setuptools-scm ];
pkgs/development/python-modules/schema-salad/default.nix-
pkgs/development/python-modules/schema-salad/default.nix-  dependencies = [
pkgs/development/python-modules/schema-salad/default.nix-    cachecontrol
pkgs/development/python-modules/schema-salad/default.nix-    mistune
--
pkgs/development/python-modules/nilearn/default.nix-  pyproject = true;
pkgs/development/python-modules/nilearn/default.nix-
--
pkgs/development/python-modules/zstandard/default.nix-  version = "0.23.0";
pkgs/development/python-modules/zstandard/default.nix-  pyproject = true;
pkgs/development/python-modules/zstandard/default.nix-
pkgs/development/python-modules/zstandard/default.nix-  src = fetchPypi {
pkgs/development/python-modules/zstandard/default.nix-    inherit pname version;
pkgs/development/python-modules/zstandard/default.nix-    hash = "sha256-stjGLQjnJV9o96dAuuhbPJuOVGa6qcv39X8c3grGvAk=";
pkgs/development/python-modules/zstandard/default.nix-  };
pkgs/development/python-modules/zstandard/default.nix-
pkgs/development/python-modules/zstandard/default.nix-  postPatch = ''
pkgs/development/python-modules/zstandard/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/zstandard/default.nix-      --replace-fail "setuptools<69.0.0" "setuptools" \
pkgs/development/python-modules/zstandard/default.nix-      --replace-fail "cffi==" "cffi>="
pkgs/development/python-modules/zstandard/default.nix-  '';
pkgs/development/python-modules/zstandard/default.nix-
pkgs/development/python-modules/zstandard/default.nix-  build-system = [
pkgs/development/python-modules/zstandard/default.nix-    cffi
pkgs/development/python-modules/zstandard/default.nix-    setuptools
pkgs/development/python-modules/zstandard/default.nix-  ];
pkgs/development/python-modules/zstandard/default.nix-
pkgs/development/python-modules/zstandard/default.nix-  dependencies = lib.optionals isPyPy [ cffi ];
--
pkgs/development/python-modules/aiowebostv/default.nix-  disabled = pythonOlder "3.11";
--
pkgs/development/python-modules/ecos/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/ecos/default.nix-    owner = "embotech";
pkgs/development/python-modules/ecos/default.nix-    repo = "ecos-python";
pkgs/development/python-modules/ecos/default.nix-    tag = "v${version}";
pkgs/development/python-modules/ecos/default.nix-    hash = "sha256-nfu1FicWr233r+VHxkQf1vqh2y4DGymJRmik8RJYJkA=";
pkgs/development/python-modules/ecos/default.nix-    fetchSubmodules = true;
pkgs/development/python-modules/ecos/default.nix-  };
pkgs/development/python-modules/ecos/default.nix-
pkgs/development/python-modules/ecos/default.nix-  postPatch = ''
pkgs/development/python-modules/ecos/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/ecos/default.nix-      --replace-fail "numpy >= 2.0.0" numpy
pkgs/development/python-modules/ecos/default.nix-  '';
pkgs/development/python-modules/ecos/default.nix-
pkgs/development/python-modules/ecos/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/ecos/default.nix-
pkgs/development/python-modules/ecos/default.nix-  dependencies = [
pkgs/development/python-modules/ecos/default.nix-    oldest-supported-numpy
pkgs/development/python-modules/ecos/default.nix-    scipy
pkgs/development/python-modules/ecos/default.nix-  ];
pkgs/development/python-modules/ecos/default.nix-
--
--
pkgs/development/python-modules/cocotb-bus/default.nix-  version = "0.2.1";
pkgs/development/python-modules/cocotb-bus/default.nix-  format = "setuptools";
pkgs/development/python-modules/cocotb-bus/default.nix-
pkgs/development/python-modules/cocotb-bus/default.nix-  src = fetchPypi {
pkgs/development/python-modules/cocotb-bus/default.nix-    inherit pname version;
pkgs/development/python-modules/cocotb-bus/default.nix-    sha256 = "a197aa4b0e0ad28469c8877b41b3fb2ec0206da9f491b9276d1578ce6dd8aa8d";
pkgs/development/python-modules/cocotb-bus/default.nix-  };
pkgs/development/python-modules/cocotb-bus/default.nix-
pkgs/development/python-modules/cocotb-bus/default.nix-  postPatch = ''
pkgs/development/python-modules/cocotb-bus/default.nix-    # remove circular dependency cocotb from setup.py
pkgs/development/python-modules/cocotb-bus/default.nix:    substituteInPlace setup.py --replace '"cocotb>=1.5.0.dev,<2.0"' ""
pkgs/development/python-modules/cocotb-bus/default.nix-  '';
pkgs/development/python-modules/cocotb-bus/default.nix-
pkgs/development/python-modules/cocotb-bus/default.nix-  # tests require cocotb, disable for now to avoid circular dependency
pkgs/development/python-modules/cocotb-bus/default.nix-  doCheck = false;
pkgs/development/python-modules/cocotb-bus/default.nix-
pkgs/development/python-modules/cocotb-bus/default.nix-  # checkPhase = ''
pkgs/development/python-modules/cocotb-bus/default.nix-  #   export PATH=$out/bin:$PATH
pkgs/development/python-modules/cocotb-bus/default.nix-  #   make test
pkgs/development/python-modules/cocotb-bus/default.nix-  # '';
pkgs/development/python-modules/cocotb-bus/default.nix-
--
pkgs/development/python-modules/aioemonitor/default.nix-  ];
pkgs/development/python-modules/aioemonitor/default.nix-
pkgs/development/python-modules/aioemonitor/default.nix-  nativeCheckInputs = [
pkgs/development/python-modules/aioemonitor/default.nix-    aioresponses
pkgs/development/python-modules/aioemonitor/default.nix-    pytest-asyncio
pkgs/development/python-modules/aioemonitor/default.nix-    pytest-raises
pkgs/development/python-modules/aioemonitor/default.nix-    pytestCheckHook
pkgs/development/python-modules/aioemonitor/default.nix-  ];
pkgs/development/python-modules/aioemonitor/default.nix-
pkgs/development/python-modules/aioemonitor/default.nix-  postPatch = ''
pkgs/development/python-modules/aioemonitor/default.nix:    substituteInPlace setup.py --replace '"pytest-runner>=5.2",' ""
pkgs/development/python-modules/aioemonitor/default.nix-  '';
pkgs/development/python-modules/aioemonitor/default.nix-
pkgs/development/python-modules/aioemonitor/default.nix-  pythonImportsCheck = [ "aioemonitor" ];
pkgs/development/python-modules/aioemonitor/default.nix-
pkgs/development/python-modules/aioemonitor/default.nix-  meta = with lib; {
pkgs/development/python-modules/aioemonitor/default.nix-    description = "Python client for SiteSage Emonitor";
pkgs/development/python-modules/aioemonitor/default.nix-    mainProgram = "my_example";
pkgs/development/python-modules/aioemonitor/default.nix-    homepage = "https://github.com/bdraco/aioemonitor";
pkgs/development/python-modules/aioemonitor/default.nix-    license = with licenses; [ asl20 ];
pkgs/development/python-modules/aioemonitor/default.nix-    maintainers = with maintainers; [ fab ];
--
pkgs/development/python-modules/usb-protocol/default.nix-
pkgs/development/python-modules/usb-protocol/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/usb-protocol/default.nix-    owner = "greatscottgadgets";
pkgs/development/python-modules/usb-protocol/default.nix-    repo = "python-usb-protocol";
pkgs/development/python-modules/usb-protocol/default.nix-    tag = version;
pkgs/development/python-modules/usb-protocol/default.nix-    hash = "sha256-lLepd2ja/UBSOARHXVwuCxLCIp0vTpUQBMdR2ovfhq8=";
pkgs/development/python-modules/usb-protocol/default.nix-  };
pkgs/development/python-modules/usb-protocol/default.nix-
pkgs/development/python-modules/usb-protocol/default.nix-  postPatch = ''
pkgs/development/python-modules/usb-protocol/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/usb-protocol/default.nix-      --replace-fail '"setuptools-git-versioning<2"' "" \
pkgs/development/python-modules/usb-protocol/default.nix-      --replace-fail 'dynamic = ["version"]' 'version = "${version}"'
pkgs/development/python-modules/usb-protocol/default.nix-  '';
pkgs/development/python-modules/usb-protocol/default.nix-
pkgs/development/python-modules/usb-protocol/default.nix-  build-system = [
pkgs/development/python-modules/usb-protocol/default.nix-    setuptools
pkgs/development/python-modules/usb-protocol/default.nix-  ];
pkgs/development/python-modules/usb-protocol/default.nix-
pkgs/development/python-modules/usb-protocol/default.nix-  dependencies = [ construct ];
pkgs/development/python-modules/usb-protocol/default.nix-
--
--
pkgs/development/python-modules/docplex/default.nix-  version = "2.30.251";
pkgs/development/python-modules/docplex/default.nix-  pyproject = true;
pkgs/development/python-modules/docplex/default.nix-
pkgs/development/python-modules/docplex/default.nix-  src = fetchPypi {
pkgs/development/python-modules/docplex/default.nix-    inherit pname version;
pkgs/development/python-modules/docplex/default.nix-    hash = "sha256-ZQMhn1tRJ1p+TnfKQzKQOw+Akl0gUDCkjT9qp8oNvyo=";
pkgs/development/python-modules/docplex/default.nix-  };
pkgs/development/python-modules/docplex/default.nix-
pkgs/development/python-modules/docplex/default.nix-  postPatch = ''
pkgs/development/python-modules/docplex/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/docplex/default.nix-      --replace-fail "setuptools~=68.2.2" "setuptools>=68.2.2"
pkgs/development/python-modules/docplex/default.nix-  '';
pkgs/development/python-modules/docplex/default.nix-
pkgs/development/python-modules/docplex/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/docplex/default.nix-
pkgs/development/python-modules/docplex/default.nix-  dependencies = [
pkgs/development/python-modules/docplex/default.nix-    docloud
pkgs/development/python-modules/docplex/default.nix-    requests
pkgs/development/python-modules/docplex/default.nix-  ];
pkgs/development/python-modules/docplex/default.nix-
--
--
pkgs/development/python-modules/bqplot/default.nix-
pkgs/development/python-modules/bqplot/default.nix-  src = fetchPypi {
pkgs/development/python-modules/bqplot/default.nix-    inherit pname version;
pkgs/development/python-modules/bqplot/default.nix-    hash = "sha256-7eAOn999kuQ8wtG5aRx9oXa2IW/dGHyOkvGde+rKXio=";
pkgs/development/python-modules/bqplot/default.nix-  };
pkgs/development/python-modules/bqplot/default.nix-
pkgs/development/python-modules/bqplot/default.nix-  # upstream seems in flux for 0.13 release. they seem to want to migrate from
pkgs/development/python-modules/bqplot/default.nix-  # jupyter_packaging to hatch, so let's patch instead of fixing upstream
pkgs/development/python-modules/bqplot/default.nix-  postPatch = ''
pkgs/development/python-modules/bqplot/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/bqplot/default.nix-      --replace "jupyter_packaging~=" "jupyter_packaging>=" \
pkgs/development/python-modules/bqplot/default.nix-      --replace "jupyterlab~=" "jupyterlab>="
pkgs/development/python-modules/bqplot/default.nix-  '';
pkgs/development/python-modules/bqplot/default.nix-
pkgs/development/python-modules/bqplot/default.nix-  build-system = [
pkgs/development/python-modules/bqplot/default.nix-    jupyter-packaging
pkgs/development/python-modules/bqplot/default.nix-    jupyterlab
pkgs/development/python-modules/bqplot/default.nix-  ];
pkgs/development/python-modules/bqplot/default.nix-
pkgs/development/python-modules/bqplot/default.nix-  dependencies = [
--
pkgs/development/python-modules/naked/default.nix-
--
pkgs/development/python-modules/pydeconz/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/pydeconz/default.nix-    owner = "Kane610";
pkgs/development/python-modules/pydeconz/default.nix-    repo = "deconz";
pkgs/development/python-modules/pydeconz/default.nix-    tag = "v${version}";
pkgs/development/python-modules/pydeconz/default.nix-    hash = "sha256-L9v6j8CFc19TlcFBTm3YCQG1nS78uIUfERB6mfwzMNM=";
pkgs/development/python-modules/pydeconz/default.nix-  };
pkgs/development/python-modules/pydeconz/default.nix-
pkgs/development/python-modules/pydeconz/default.nix-  postPatch = ''
pkgs/development/python-modules/pydeconz/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/pydeconz/default.nix-      --replace-fail "setuptools==77.0.3" "setuptools" \
pkgs/development/python-modules/pydeconz/default.nix-      --replace-fail "wheel==" "wheel>="
pkgs/development/python-modules/pydeconz/default.nix-  '';
pkgs/development/python-modules/pydeconz/default.nix-
pkgs/development/python-modules/pydeconz/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/pydeconz/default.nix-
pkgs/development/python-modules/pydeconz/default.nix-  dependencies = [
pkgs/development/python-modules/pydeconz/default.nix-    aiohttp
pkgs/development/python-modules/pydeconz/default.nix-    orjson
pkgs/development/python-modules/pydeconz/default.nix-  ];
--
pkgs/development/python-modules/plotly/default.nix-  pyproject = true;
--
pkgs/development/python-modules/wfuzz/default.nix-    # replace use of imp module for Python 3.12
pkgs/development/python-modules/wfuzz/default.nix-    # https://github.com/xmendez/wfuzz/pull/365
pkgs/development/python-modules/wfuzz/default.nix-    (fetchpatch2 {
pkgs/development/python-modules/wfuzz/default.nix-      url = "https://github.com/xmendez/wfuzz/commit/f4c028b9ada4c36dabf3bc752f69f6ddc110920f.patch?full_index=1";
pkgs/development/python-modules/wfuzz/default.nix-      hash = "sha256-t7pUMcdFmwAsGUNBRdZr+Jje/yR0yzeGIgeYNEq4hFE=";
pkgs/development/python-modules/wfuzz/default.nix-    })
pkgs/development/python-modules/wfuzz/default.nix-  ];
pkgs/development/python-modules/wfuzz/default.nix-
pkgs/development/python-modules/wfuzz/default.nix-  postPatch = ''
pkgs/development/python-modules/wfuzz/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/wfuzz/default.nix-      --replace-fail "pyparsing>=2.4*" "pyparsing>=2.4"
pkgs/development/python-modules/wfuzz/default.nix-  '';
pkgs/development/python-modules/wfuzz/default.nix-
pkgs/development/python-modules/wfuzz/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/wfuzz/default.nix-
pkgs/development/python-modules/wfuzz/default.nix-  dependencies = [
pkgs/development/python-modules/wfuzz/default.nix-    chardet
pkgs/development/python-modules/wfuzz/default.nix-    distutils # src/wfuzz/plugin_api/base.py
pkgs/development/python-modules/wfuzz/default.nix-    pycurl
pkgs/development/python-modules/wfuzz/default.nix-    six
--
--
pkgs/development/python-modules/deepwave/default.nix-    rev = "v${version}";
pkgs/development/python-modules/deepwave/default.nix-    hash = "sha256-DOOy+B12jgwJzQ90qzX50OFxYLPRcVdVYSE5gi3pqDM=";
pkgs/development/python-modules/deepwave/default.nix-  };
pkgs/development/python-modules/deepwave/default.nix-
pkgs/development/python-modules/deepwave/default.nix-  # unable to find ninja although it is available, most likely because it looks for its pip version
pkgs/development/python-modules/deepwave/default.nix-  postPatch = ''
pkgs/development/python-modules/deepwave/default.nix:    substituteInPlace setup.cfg --replace "ninja" ""
pkgs/development/python-modules/deepwave/default.nix-
pkgs/development/python-modules/deepwave/default.nix-    # Adding ninja to the path forcibly
pkgs/development/python-modules/deepwave/default.nix-    mv src/deepwave/__init__.py tmp
pkgs/development/python-modules/deepwave/default.nix-    echo "${linePatch}" > src/deepwave/__init__.py
pkgs/development/python-modules/deepwave/default.nix-    cat tmp >> src/deepwave/__init__.py
pkgs/development/python-modules/deepwave/default.nix-    rm tmp
pkgs/development/python-modules/deepwave/default.nix-  '';
pkgs/development/python-modules/deepwave/default.nix-
pkgs/development/python-modules/deepwave/default.nix-  # The source files are compiled at runtime and cached at the
pkgs/development/python-modules/deepwave/default.nix-  # $HOME/.cache folder, so for the check phase it is needed to
--
pkgs/development/python-modules/ansible-runner/default.nix-  pyproject = true;
pkgs/development/python-modules/ansible-runner/default.nix-
pkgs/development/python-modules/ansible-runner/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/ansible-runner/default.nix-    owner = "ansible";
pkgs/development/python-modules/ansible-runner/default.nix-    repo = "ansible-runner";
pkgs/development/python-modules/ansible-runner/default.nix-    tag = version;
pkgs/development/python-modules/ansible-runner/default.nix-    hash = "sha256-Fyavc13TRHbslRVoBawyBgvUKhuIZsxBc7go66axE0Y=";
pkgs/development/python-modules/ansible-runner/default.nix-  };
pkgs/development/python-modules/ansible-runner/default.nix-
pkgs/development/python-modules/ansible-runner/default.nix-  postPatch = ''
pkgs/development/python-modules/ansible-runner/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/ansible-runner/default.nix-      --replace-fail "setuptools>=45, <=70.0.0" setuptools \
pkgs/development/python-modules/ansible-runner/default.nix-      --replace-fail "setuptools-scm[toml]>=6.2, <=8.1.0" setuptools-scm
pkgs/development/python-modules/ansible-runner/default.nix-  '';
pkgs/development/python-modules/ansible-runner/default.nix-
pkgs/development/python-modules/ansible-runner/default.nix-  build-system = [
pkgs/development/python-modules/ansible-runner/default.nix-    setuptools
pkgs/development/python-modules/ansible-runner/default.nix-    setuptools-scm
pkgs/development/python-modules/ansible-runner/default.nix-  ];
pkgs/development/python-modules/ansible-runner/default.nix-
pkgs/development/python-modules/ansible-runner/default.nix-  dependencies = [
--
pkgs/development/python-modules/verilogae/default.nix-  pyproject = true;
--
pkgs/development/python-modules/pytest-annotate/default.nix-    inherit pname version;
pkgs/development/python-modules/pytest-annotate/default.nix-    hash = "sha256-CSaTIPjSGHKCR0Nvet6W8zzz/oWEC0BjIULZ+JaMH9A=";
pkgs/development/python-modules/pytest-annotate/default.nix-  };
pkgs/development/python-modules/pytest-annotate/default.nix-
pkgs/development/python-modules/pytest-annotate/default.nix-  buildInputs = [ pytest ];
pkgs/development/python-modules/pytest-annotate/default.nix-
pkgs/development/python-modules/pytest-annotate/default.nix-  propagatedBuildInputs = [ pyannotate ];
pkgs/development/python-modules/pytest-annotate/default.nix-
pkgs/development/python-modules/pytest-annotate/default.nix-  postPatch = ''
pkgs/development/python-modules/pytest-annotate/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/pytest-annotate/default.nix-      --replace "pytest>=3.2.0,<7.0.0" "pytest>=3.2.0"
pkgs/development/python-modules/pytest-annotate/default.nix-  '';
pkgs/development/python-modules/pytest-annotate/default.nix-
pkgs/development/python-modules/pytest-annotate/default.nix-  # Module has no tests
pkgs/development/python-modules/pytest-annotate/default.nix-  doCheck = false;
pkgs/development/python-modules/pytest-annotate/default.nix-
pkgs/development/python-modules/pytest-annotate/default.nix-  pythonImportsCheck = [ "pytest_annotate" ];
pkgs/development/python-modules/pytest-annotate/default.nix-
pkgs/development/python-modules/pytest-annotate/default.nix-  meta = with lib; {
pkgs/development/python-modules/pytest-annotate/default.nix-    description = "Generate PyAnnotate annotations from your pytest tests";
--
--
pkgs/development/python-modules/aiohasupervisor/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/aiohasupervisor/default.nix-    owner = "home-assistant-libs";
pkgs/development/python-modules/aiohasupervisor/default.nix-    repo = "python-supervisor-client";
pkgs/development/python-modules/aiohasupervisor/default.nix-    tag = version;
pkgs/development/python-modules/aiohasupervisor/default.nix-    hash = "sha256-CrcLyG8fpThYHFHH2w+UAlGxuqwpUCWsYUx2gaW9RLw=";
pkgs/development/python-modules/aiohasupervisor/default.nix-  };
pkgs/development/python-modules/aiohasupervisor/default.nix-
pkgs/development/python-modules/aiohasupervisor/default.nix-  postPatch = ''
pkgs/development/python-modules/aiohasupervisor/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/aiohasupervisor/default.nix-      --replace-fail 'version = "0.0.0"' 'version = "${version}"' \
pkgs/development/python-modules/aiohasupervisor/default.nix-      --replace-fail 'setuptools>=68.0,<79.1' setuptools
pkgs/development/python-modules/aiohasupervisor/default.nix-  '';
pkgs/development/python-modules/aiohasupervisor/default.nix-
pkgs/development/python-modules/aiohasupervisor/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/aiohasupervisor/default.nix-
pkgs/development/python-modules/aiohasupervisor/default.nix-  dependencies = [
pkgs/development/python-modules/aiohasupervisor/default.nix-    aiohttp
pkgs/development/python-modules/aiohasupervisor/default.nix-    mashumaro
pkgs/development/python-modules/aiohasupervisor/default.nix-    orjson
--
pkgs/development/python-modules/skein/default.nix-  ++ lib.optionals (!pythonOlder "3.12") [ setuptools ];
--
pkgs/development/python-modules/shap/default.nix-
pkgs/development/python-modules/shap/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/shap/default.nix-    owner = "slundberg";
pkgs/development/python-modules/shap/default.nix-    repo = "shap";
pkgs/development/python-modules/shap/default.nix-    tag = "v${version}";
pkgs/development/python-modules/shap/default.nix-    hash = "sha256-eWZhyrFpEFlmTFPTHZng9V+uMRMXDVzFdgrqIzRQTws=";
pkgs/development/python-modules/shap/default.nix-  };
pkgs/development/python-modules/shap/default.nix-
pkgs/development/python-modules/shap/default.nix-  postPatch = ''
pkgs/development/python-modules/shap/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/shap/default.nix-      --replace-fail "cython>=3.0.11" cython \
pkgs/development/python-modules/shap/default.nix-      --replace-fail "numpy>=2.0" "numpy"
pkgs/development/python-modules/shap/default.nix-  '';
pkgs/development/python-modules/shap/default.nix-
pkgs/development/python-modules/shap/default.nix-  build-system = [
pkgs/development/python-modules/shap/default.nix-    cython
pkgs/development/python-modules/shap/default.nix-    numpy
pkgs/development/python-modules/shap/default.nix-    setuptools
pkgs/development/python-modules/shap/default.nix-    setuptools-scm
pkgs/development/python-modules/shap/default.nix-  ];
--
pkgs/development/python-modules/pysnow/default.nix-  patches = [
--
pkgs/development/python-modules/statsmodels/default.nix-  version = "0.14.5";
pkgs/development/python-modules/statsmodels/default.nix-  pyproject = true;
pkgs/development/python-modules/statsmodels/default.nix-
pkgs/development/python-modules/statsmodels/default.nix-  src = fetchPypi {
pkgs/development/python-modules/statsmodels/default.nix-    inherit pname version;
pkgs/development/python-modules/statsmodels/default.nix-    hash = "sha256-3iYOWMzP0s7d+DW1WjVyM9bKhToapPkPdVOlLMccbd8=";
pkgs/development/python-modules/statsmodels/default.nix-  };
pkgs/development/python-modules/statsmodels/default.nix-
pkgs/development/python-modules/statsmodels/default.nix-  postPatch = ''
pkgs/development/python-modules/statsmodels/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/statsmodels/default.nix-      --replace-fail 'setuptools_scm[toml]>=8,<9' 'setuptools_scm[toml]'
pkgs/development/python-modules/statsmodels/default.nix-  '';
pkgs/development/python-modules/statsmodels/default.nix-
pkgs/development/python-modules/statsmodels/default.nix-  build-system = [
pkgs/development/python-modules/statsmodels/default.nix-    cython
pkgs/development/python-modules/statsmodels/default.nix-    numpy
pkgs/development/python-modules/statsmodels/default.nix-    scipy
pkgs/development/python-modules/statsmodels/default.nix-    setuptools
pkgs/development/python-modules/statsmodels/default.nix-    setuptools-scm
pkgs/development/python-modules/statsmodels/default.nix-  ];
--
--
pkgs/development/python-modules/rapidfuzz/default.nix-    # https://github.com/rapidfuzz/RapidFuzz/pull/446
pkgs/development/python-modules/rapidfuzz/default.nix-    (fetchpatch {
pkgs/development/python-modules/rapidfuzz/default.nix-      name = "support-taskflow-3.10.0.patch";
pkgs/development/python-modules/rapidfuzz/default.nix-      url = "https://github.com/rapidfuzz/RapidFuzz/commit/bba3281cc61ecc4ab4affe5d2d50389a4f6d7556.patch";
pkgs/development/python-modules/rapidfuzz/default.nix-      hash = "sha256-kAS6xsPY7eUTfKO+EAOW8bktY4cApvLEpRMciJEsPgk=";
pkgs/development/python-modules/rapidfuzz/default.nix-    })
pkgs/development/python-modules/rapidfuzz/default.nix-  ];
pkgs/development/python-modules/rapidfuzz/default.nix-
pkgs/development/python-modules/rapidfuzz/default.nix-  postPatch = ''
pkgs/development/python-modules/rapidfuzz/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/rapidfuzz/default.nix-      --replace-fail "Cython >=3.0.12, <3.1.0" Cython
pkgs/development/python-modules/rapidfuzz/default.nix-  '';
pkgs/development/python-modules/rapidfuzz/default.nix-
pkgs/development/python-modules/rapidfuzz/default.nix-  build-system = [
pkgs/development/python-modules/rapidfuzz/default.nix-    cmake
pkgs/development/python-modules/rapidfuzz/default.nix-    cython
pkgs/development/python-modules/rapidfuzz/default.nix-    ninja
pkgs/development/python-modules/rapidfuzz/default.nix-    scikit-build-core
pkgs/development/python-modules/rapidfuzz/default.nix-  ];
pkgs/development/python-modules/rapidfuzz/default.nix-
--
--
--
pkgs/development/python-modules/napalm/hp-procurve.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/napalm/hp-procurve.nix-    owner = "napalm-automation-community";
pkgs/development/python-modules/napalm/hp-procurve.nix-    repo = "napalm-hp-procurve";
pkgs/development/python-modules/napalm/hp-procurve.nix-    tag = version;
pkgs/development/python-modules/napalm/hp-procurve.nix-    hash = "sha256-cO4kxI90krj1knzixRKWxa77OAaxjO8dLTy02VpkV9M=";
pkgs/development/python-modules/napalm/hp-procurve.nix-  };
pkgs/development/python-modules/napalm/hp-procurve.nix-
pkgs/development/python-modules/napalm/hp-procurve.nix-  patchPhase = ''
pkgs/development/python-modules/napalm/hp-procurve.nix-    # Dependency installation in setup.py doesn't work
pkgs/development/python-modules/napalm/hp-procurve.nix-    echo -n > requirements.txt
pkgs/development/python-modules/napalm/hp-procurve.nix:    substituteInPlace setup.cfg \
pkgs/development/python-modules/napalm/hp-procurve.nix-      --replace " --pylama" ""
pkgs/development/python-modules/napalm/hp-procurve.nix-  '';
pkgs/development/python-modules/napalm/hp-procurve.nix-
pkgs/development/python-modules/napalm/hp-procurve.nix-  build-system = [
pkgs/development/python-modules/napalm/hp-procurve.nix-    setuptools
pkgs/development/python-modules/napalm/hp-procurve.nix-    pip
pkgs/development/python-modules/napalm/hp-procurve.nix-  ];
pkgs/development/python-modules/napalm/hp-procurve.nix-
pkgs/development/python-modules/napalm/hp-procurve.nix-  buildInputs = [ napalm ];
--
pkgs/development/python-modules/vbuild/default.nix-    owner = "manatlan";
pkgs/development/python-modules/vbuild/default.nix-    repo = "vbuild";
pkgs/development/python-modules/vbuild/default.nix-    rev = "refs/tags/v${version}";
pkgs/development/python-modules/vbuild/default.nix-    hash = "sha256-p9v1FiYn0cI+f/25hvjwm7eb1GqxXvNnmXBGwZe9fk0=";
pkgs/development/python-modules/vbuild/default.nix-  };
pkgs/development/python-modules/vbuild/default.nix-
pkgs/development/python-modules/vbuild/default.nix-  postPatch = ''
pkgs/development/python-modules/vbuild/default.nix-    # Switch to poetry-core, patch can't be applied, https://github.com/manatlan/vbuild/pull/12
pkgs/development/python-modules/vbuild/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/vbuild/default.nix-      --replace-fail 'version = "0.0.0"' 'version = "${version}"' \
pkgs/development/python-modules/vbuild/default.nix-      --replace-fail 'requires = ["poetry>=0.12"]' 'requires = ["poetry-core>=1.0.0"]' \
pkgs/development/python-modules/vbuild/default.nix-      --replace-fail 'build-backend = "poetry.masonry.api"' 'build-backend = "poetry.core.masonry.api"'
pkgs/development/python-modules/vbuild/default.nix-  '';
pkgs/development/python-modules/vbuild/default.nix-
pkgs/development/python-modules/vbuild/default.nix-  build-system = [ poetry-core ];
pkgs/development/python-modules/vbuild/default.nix-
pkgs/development/python-modules/vbuild/default.nix-  dependencies = [ pscript ];
pkgs/development/python-modules/vbuild/default.nix-
pkgs/development/python-modules/vbuild/default.nix-  nativeCheckInputs = [ pytestCheckHook ];
--
pkgs/development/python-modules/pytest-xprocess/default.nix-  version = "1.0.2";
--
pkgs/development/python-modules/stim/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/stim/default.nix-    owner = "quantumlib";
pkgs/development/python-modules/stim/default.nix-    repo = "Stim";
pkgs/development/python-modules/stim/default.nix-    tag = "v${version}";
pkgs/development/python-modules/stim/default.nix-    hash = "sha256-Wls7dJkuV/RXnMizwrYOJOKopWEf1r21FKoKHjmpEQ0=";
pkgs/development/python-modules/stim/default.nix-  };
pkgs/development/python-modules/stim/default.nix-
pkgs/development/python-modules/stim/default.nix-  postPatch = ''
pkgs/development/python-modules/stim/default.nix-    # asked to relax this in https://github.com/quantumlib/Stim/issues/623
pkgs/development/python-modules/stim/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/stim/default.nix-      --replace-quiet "pybind11~=" "pybind11>="
pkgs/development/python-modules/stim/default.nix-
pkgs/development/python-modules/stim/default.nix-    # Simple workgroud about https://github.com/networkx/networkx/pull/4829
pkgs/development/python-modules/stim/default.nix-    # https://github.com/quantumlib/Stim/commit/c0dd0b1c8125b2096cd54b6f72884a459e47fe3e
pkgs/development/python-modules/stim/default.nix:    substituteInPlace glue/lattice_surgery/stimzx/_zx_graph_solver.py \
pkgs/development/python-modules/stim/default.nix-      --replace-fail "networkx.testing.assert_graphs_equal" "assert networkx.utils.edges_equal"
pkgs/development/python-modules/stim/default.nix-
pkgs/development/python-modules/stim/default.nix:    substituteInPlace glue/lattice_surgery/stimzx/_text_diagram_parsing.py \
pkgs/development/python-modules/stim/default.nix-      --replace-fail "nx.testing.assert_graphs_equal" "assert nx.utils.edges_equal"
pkgs/development/python-modules/stim/default.nix-
pkgs/development/python-modules/stim/default.nix:    substituteInPlace glue/lattice_surgery/stimzx/_text_diagram_parsing_test.py \
--
pkgs/development/python-modules/ruyaml/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/ruyaml/default.nix-    owner = "pycontribs";
pkgs/development/python-modules/ruyaml/default.nix-    repo = "ruyaml";
pkgs/development/python-modules/ruyaml/default.nix-    tag = "v${version}";
pkgs/development/python-modules/ruyaml/default.nix-    hash = "sha256-A37L/voBrn2aZ7xT8+bWdZJxbWRjnxbstQtSyUeN1sA=";
pkgs/development/python-modules/ruyaml/default.nix-  };
pkgs/development/python-modules/ruyaml/default.nix-
pkgs/development/python-modules/ruyaml/default.nix-  postPatch = ''
pkgs/development/python-modules/ruyaml/default.nix-    # https://github.com/pycontribs/ruyaml/pull/107
pkgs/development/python-modules/ruyaml/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/ruyaml/default.nix-      --replace '"pip >= 19.3.1",' "" \
pkgs/development/python-modules/ruyaml/default.nix-      --replace '"setuptools_scm_git_archive >= 1.1",' ""
pkgs/development/python-modules/ruyaml/default.nix-  '';
pkgs/development/python-modules/ruyaml/default.nix-
pkgs/development/python-modules/ruyaml/default.nix-  nativeBuildInputs = [ setuptools-scm ];
pkgs/development/python-modules/ruyaml/default.nix-
pkgs/development/python-modules/ruyaml/default.nix-  propagatedBuildInputs = [ distro ];
pkgs/development/python-modules/ruyaml/default.nix-
pkgs/development/python-modules/ruyaml/default.nix-  nativeCheckInputs = [ pytestCheckHook ];
pkgs/development/python-modules/ruyaml/default.nix-
--
pkgs/development/python-modules/pymoo/default.nix-  pyproject = true;
--
pkgs/development/python-modules/gradient-utils/default.nix-    mock
pkgs/development/python-modules/gradient-utils/default.nix-    requests
pkgs/development/python-modules/gradient-utils/default.nix-    pytestCheckHook
pkgs/development/python-modules/gradient-utils/default.nix-  ];
pkgs/development/python-modules/gradient-utils/default.nix-
pkgs/development/python-modules/gradient-utils/default.nix-  postPatch = ''
pkgs/development/python-modules/gradient-utils/default.nix-    # https://github.com/Paperspace/gradient-utils/issues/68
pkgs/development/python-modules/gradient-utils/default.nix-    # https://github.com/Paperspace/gradient-utils/issues/72
pkgs/development/python-modules/gradient-utils/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/gradient-utils/default.nix-      --replace 'wheel = "^0.35.1"' 'wheel = "*"' \
pkgs/development/python-modules/gradient-utils/default.nix-      --replace 'prometheus-client = ">=0.8,<0.10"' 'prometheus-client = "*"' \
pkgs/development/python-modules/gradient-utils/default.nix-      --replace 'pymongo = "^3.11.0"' 'pymongo = ">=3.11.0"'
pkgs/development/python-modules/gradient-utils/default.nix-  '';
pkgs/development/python-modules/gradient-utils/default.nix-
pkgs/development/python-modules/gradient-utils/default.nix-  preCheck = ''
pkgs/development/python-modules/gradient-utils/default.nix-    export HOSTNAME=myhost-experimentId
pkgs/development/python-modules/gradient-utils/default.nix-  '';
pkgs/development/python-modules/gradient-utils/default.nix-
pkgs/development/python-modules/gradient-utils/default.nix-  disabledTestPaths = [
--
pkgs/development/python-modules/libasyncns/default.nix-  format = "setuptools";
pkgs/development/python-modules/libasyncns/default.nix-
pkgs/development/python-modules/libasyncns/default.nix-  src = fetchurl {
pkgs/development/python-modules/libasyncns/default.nix-    url = "https://launchpad.net/libasyncns-python/trunk/${version}/+download/libasyncns-python-${version}.tar.bz2";
pkgs/development/python-modules/libasyncns/default.nix-    sha256 = "1q4l71b2h9q756x4pjynp6kczr2d8c1jvbdp982hf7xzv7w5gxqg";
pkgs/development/python-modules/libasyncns/default.nix-  };
pkgs/development/python-modules/libasyncns/default.nix-
pkgs/development/python-modules/libasyncns/default.nix-  patches = [ ./libasyncns-fix-res-consts.patch ];
pkgs/development/python-modules/libasyncns/default.nix-
pkgs/development/python-modules/libasyncns/default.nix-  postPatch = lib.optionalString stdenv.hostPlatform.isDarwin ''
pkgs/development/python-modules/libasyncns/default.nix:    substituteInPlace resquery.c \
pkgs/development/python-modules/libasyncns/default.nix-      --replace '<arpa/nameser.h>' '<arpa/nameser_compat.h>'
pkgs/development/python-modules/libasyncns/default.nix-  '';
pkgs/development/python-modules/libasyncns/default.nix-
pkgs/development/python-modules/libasyncns/default.nix-  buildInputs = [ libasyncns ];
pkgs/development/python-modules/libasyncns/default.nix-  nativeBuildInputs = [ pkg-config ];
pkgs/development/python-modules/libasyncns/default.nix-  doCheck = false; # requires network access
pkgs/development/python-modules/libasyncns/default.nix-
pkgs/development/python-modules/libasyncns/default.nix-  pythonImportsCheck = [ "libasyncns" ];
pkgs/development/python-modules/libasyncns/default.nix-
pkgs/development/python-modules/libasyncns/default.nix-  meta = with lib; {
--
--
pkgs/development/python-modules/pyuptimerobot/default.nix-  ];
--
pkgs/development/python-modules/zetup/default.nix-  # https://github.com/zimmermanncode/zetup/issues/4
pkgs/development/python-modules/zetup/default.nix-  disabled = pythonAtLeast "3.10";
pkgs/development/python-modules/zetup/default.nix-
pkgs/development/python-modules/zetup/default.nix-  src = fetchPypi {
pkgs/development/python-modules/zetup/default.nix-    inherit pname version;
pkgs/development/python-modules/zetup/default.nix-    sha256 = "b8a9bdcfa4b705d72b55b218658bc9403c157db7b57a14158253c98d03ab713d";
pkgs/development/python-modules/zetup/default.nix-  };
pkgs/development/python-modules/zetup/default.nix-
pkgs/development/python-modules/zetup/default.nix-  # Python > 3.7 compatibility
pkgs/development/python-modules/zetup/default.nix-  postPatch = ''
pkgs/development/python-modules/zetup/default.nix:    substituteInPlace zetup/zetup_config.py \
pkgs/development/python-modules/zetup/default.nix-      --replace "'3.7']" "'3.7', '3.8', '3.9', '3.10']"
pkgs/development/python-modules/zetup/default.nix-  '';
pkgs/development/python-modules/zetup/default.nix-
pkgs/development/python-modules/zetup/default.nix-  checkPhase = ''
pkgs/development/python-modules/zetup/default.nix-    py.test test -k "not TestObject" --deselect=test/test_zetup_config.py::test_classifiers
pkgs/development/python-modules/zetup/default.nix-  '';
pkgs/development/python-modules/zetup/default.nix-
pkgs/development/python-modules/zetup/default.nix-  propagatedBuildInputs = [ setuptools-scm ];
--
pkgs/development/python-modules/invocations/default.nix-    owner = "pyinvoke";
pkgs/development/python-modules/invocations/default.nix-    repo = "invocations";
pkgs/development/python-modules/invocations/default.nix-    tag = version;
pkgs/development/python-modules/invocations/default.nix-    hash = "sha256-JnhdcxhBNsYgDMcljtGKjOT1agujlao/66QifGuh6I0=";
pkgs/development/python-modules/invocations/default.nix-  };
pkgs/development/python-modules/invocations/default.nix-
pkgs/development/python-modules/invocations/default.nix-  patches = [ ./replace-blessings-with-blessed.patch ];
pkgs/development/python-modules/invocations/default.nix-
pkgs/development/python-modules/invocations/default.nix-  postPatch = ''
pkgs/development/python-modules/invocations/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/invocations/default.nix-      --replace "semantic_version>=2.4,<2.7" "semantic_version"
pkgs/development/python-modules/invocations/default.nix-  '';
pkgs/development/python-modules/invocations/default.nix-
pkgs/development/python-modules/invocations/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/invocations/default.nix-    blessed
pkgs/development/python-modules/invocations/default.nix-    invoke
pkgs/development/python-modules/invocations/default.nix-    releases
pkgs/development/python-modules/invocations/default.nix-    semantic-version
pkgs/development/python-modules/invocations/default.nix-    tabulate
pkgs/development/python-modules/invocations/default.nix-    tqdm
--
--
pkgs/development/python-modules/brian2/default.nix-    inherit pname version;
pkgs/development/python-modules/brian2/default.nix-    hash = "sha256-5N3uwcwj83VC49BnrOoncGI8Jk+97RRMptehtsw8o5c=";
pkgs/development/python-modules/brian2/default.nix-  };
pkgs/development/python-modules/brian2/default.nix-
pkgs/development/python-modules/brian2/default.nix-  patches = [
pkgs/development/python-modules/brian2/default.nix-    ./0001-remove-invalidxyz.patch # invalidxyz are reported as error so I remove it
pkgs/development/python-modules/brian2/default.nix-  ];
pkgs/development/python-modules/brian2/default.nix-
pkgs/development/python-modules/brian2/default.nix-  postPatch = ''
pkgs/development/python-modules/brian2/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/brian2/default.nix-      --replace-fail "numpy>=2.0.0rc1" "numpy"
pkgs/development/python-modules/brian2/default.nix-
pkgs/development/python-modules/brian2/default.nix:    substituteInPlace brian2/codegen/cpp_prefs.py \
pkgs/development/python-modules/brian2/default.nix-      --replace-fail "distutils" "setuptools._distutils"
pkgs/development/python-modules/brian2/default.nix-  '';
pkgs/development/python-modules/brian2/default.nix-
pkgs/development/python-modules/brian2/default.nix-  build-system = [
pkgs/development/python-modules/brian2/default.nix-    setuptools-scm
pkgs/development/python-modules/brian2/default.nix-  ];
pkgs/development/python-modules/brian2/default.nix-
pkgs/development/python-modules/brian2/default.nix-  dependencies = [
--
pkgs/development/python-modules/tesserocr/default.nix-      url = "https://github.com/sirfz/tesserocr/commit/78d9e8187bd4d282d572bd5221db2c69e560e017.patch";
pkgs/development/python-modules/tesserocr/default.nix-      hash = "sha256-s51s9EIV9AZT6UoqwTuQ8lOjToqwIIUkDLjsvCsyYFU=";
pkgs/development/python-modules/tesserocr/default.nix-    })
pkgs/development/python-modules/tesserocr/default.nix-  ];
pkgs/development/python-modules/tesserocr/default.nix-
pkgs/development/python-modules/tesserocr/default.nix-  # https://github.com/sirfz/tesserocr/issues/314
pkgs/development/python-modules/tesserocr/default.nix-  postPatch = ''
pkgs/development/python-modules/tesserocr/default.nix-    sed -i '/allheaders.h/a\    pass\n\ncdef extern from "leptonica/pix_internal.h" nogil:' tesserocr/tesseract.pxd
pkgs/development/python-modules/tesserocr/default.nix-
pkgs/development/python-modules/tesserocr/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/tesserocr/default.nix-      --replace-fail "Cython>=0.23,<3.1.0" Cython
pkgs/development/python-modules/tesserocr/default.nix-  '';
pkgs/development/python-modules/tesserocr/default.nix-
pkgs/development/python-modules/tesserocr/default.nix-  build-system = [
pkgs/development/python-modules/tesserocr/default.nix-    cython
pkgs/development/python-modules/tesserocr/default.nix-    pkg-config
pkgs/development/python-modules/tesserocr/default.nix-    setuptools
pkgs/development/python-modules/tesserocr/default.nix-  ];
pkgs/development/python-modules/tesserocr/default.nix-
pkgs/development/python-modules/tesserocr/default.nix-  buildInputs = [
--
--
pkgs/development/python-modules/monai/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/monai/default.nix-    owner = "Project-MONAI";
pkgs/development/python-modules/monai/default.nix-    repo = "MONAI";
pkgs/development/python-modules/monai/default.nix-    tag = version;
pkgs/development/python-modules/monai/default.nix-    hash = "sha256-SUZSWChO0oQlLblPwmCg2zt2Jp5QnpM1CXWnMiOiLhw=";
pkgs/development/python-modules/monai/default.nix-    # note: upstream consistently seems to modify the tag shortly after release,
pkgs/development/python-modules/monai/default.nix-    # so best to wait a few days before updating
pkgs/development/python-modules/monai/default.nix-  };
pkgs/development/python-modules/monai/default.nix-
pkgs/development/python-modules/monai/default.nix-  postPatch = ''
pkgs/development/python-modules/monai/default.nix:    substituteInPlace pyproject.toml --replace-fail 'torch>=2.4.1, <2.7.0' 'torch'
pkgs/development/python-modules/monai/default.nix-  '';
pkgs/development/python-modules/monai/default.nix-
pkgs/development/python-modules/monai/default.nix-  preBuild = ''
pkgs/development/python-modules/monai/default.nix-    export MAX_JOBS=$NIX_BUILD_CORES;
pkgs/development/python-modules/monai/default.nix-  '';
pkgs/development/python-modules/monai/default.nix-
pkgs/development/python-modules/monai/default.nix-  build-system = [
pkgs/development/python-modules/monai/default.nix-    ninja
pkgs/development/python-modules/monai/default.nix-    which
pkgs/development/python-modules/monai/default.nix-  ];
--
pkgs/development/python-modules/jupyter-collaboration-ui/default.nix-  pyproject = true;
pkgs/development/python-modules/jupyter-collaboration-ui/default.nix-
pkgs/development/python-modules/jupyter-collaboration-ui/default.nix-  src = fetchPypi {
pkgs/development/python-modules/jupyter-collaboration-ui/default.nix-    pname = "jupyter_collaboration_ui";
pkgs/development/python-modules/jupyter-collaboration-ui/default.nix-    inherit version;
pkgs/development/python-modules/jupyter-collaboration-ui/default.nix-    hash = "sha256-EaoXDM1kcpzXyRFEtP9NLo2QAn1U44FXAX61NemdfMk=";
pkgs/development/python-modules/jupyter-collaboration-ui/default.nix-  };
pkgs/development/python-modules/jupyter-collaboration-ui/default.nix-
pkgs/development/python-modules/jupyter-collaboration-ui/default.nix-  postPatch = ''
pkgs/development/python-modules/jupyter-collaboration-ui/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/jupyter-collaboration-ui/default.nix-      --replace-fail ', "jupyterlab>=4.0.0"' ""
pkgs/development/python-modules/jupyter-collaboration-ui/default.nix-  '';
pkgs/development/python-modules/jupyter-collaboration-ui/default.nix-
pkgs/development/python-modules/jupyter-collaboration-ui/default.nix-  build-system = [
pkgs/development/python-modules/jupyter-collaboration-ui/default.nix-    hatchling
pkgs/development/python-modules/jupyter-collaboration-ui/default.nix-    hatch-jupyter-builder
pkgs/development/python-modules/jupyter-collaboration-ui/default.nix-  ];
pkgs/development/python-modules/jupyter-collaboration-ui/default.nix-
pkgs/development/python-modules/jupyter-collaboration-ui/default.nix-  pythonImportsCheck = [ "jupyter_collaboration_ui" ];
pkgs/development/python-modules/jupyter-collaboration-ui/default.nix-
--
--
pkgs/development/python-modules/aioazuredevops/default.nix-
pkgs/development/python-modules/aioazuredevops/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/aioazuredevops/default.nix-    owner = "timmo001";
pkgs/development/python-modules/aioazuredevops/default.nix-    repo = "aioazuredevops";
pkgs/development/python-modules/aioazuredevops/default.nix-    tag = version;
pkgs/development/python-modules/aioazuredevops/default.nix-    hash = "sha256-RZBiFPzYtEoc51T3irVHL9xVlZgACyM2lu1TkMoatqU=";
pkgs/development/python-modules/aioazuredevops/default.nix-  };
pkgs/development/python-modules/aioazuredevops/default.nix-
pkgs/development/python-modules/aioazuredevops/default.nix-  postPatch = ''
pkgs/development/python-modules/aioazuredevops/default.nix:    substituteInPlace requirements_setup.txt \
pkgs/development/python-modules/aioazuredevops/default.nix-      --replace-fail "==" ">="
pkgs/development/python-modules/aioazuredevops/default.nix-  '';
pkgs/development/python-modules/aioazuredevops/default.nix-
pkgs/development/python-modules/aioazuredevops/default.nix-  build-system = [
pkgs/development/python-modules/aioazuredevops/default.nix-    incremental
pkgs/development/python-modules/aioazuredevops/default.nix-    setuptools
pkgs/development/python-modules/aioazuredevops/default.nix-  ];
pkgs/development/python-modules/aioazuredevops/default.nix-
pkgs/development/python-modules/aioazuredevops/default.nix-  dependencies = [
pkgs/development/python-modules/aioazuredevops/default.nix-    aiohttp
--
--
pkgs/development/python-modules/docformatter/default.nix-    owner = "PyCQA";
pkgs/development/python-modules/docformatter/default.nix-    repo = "docformatter";
pkgs/development/python-modules/docformatter/default.nix-    tag = "v${version}";
pkgs/development/python-modules/docformatter/default.nix-    hash = "sha256-eLjaHso1p/nD9K0E+HkeBbnCnvjZ1sdpfww9tzBh0TI=";
pkgs/development/python-modules/docformatter/default.nix-  };
pkgs/development/python-modules/docformatter/default.nix-
pkgs/development/python-modules/docformatter/default.nix-  patches = [ ./test-path.patch ];
pkgs/development/python-modules/docformatter/default.nix-
pkgs/development/python-modules/docformatter/default.nix-  postPatch = ''
pkgs/development/python-modules/docformatter/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/docformatter/default.nix-      --replace 'charset_normalizer = "^2.0.0"' 'charset_normalizer = ">=2.0.0"'
pkgs/development/python-modules/docformatter/default.nix:    substituteInPlace tests/conftest.py \
pkgs/development/python-modules/docformatter/default.nix-      --subst-var-by docformatter $out/bin/docformatter
pkgs/development/python-modules/docformatter/default.nix-  '';
pkgs/development/python-modules/docformatter/default.nix-
pkgs/development/python-modules/docformatter/default.nix-  nativeBuildInputs = [ poetry-core ];
pkgs/development/python-modules/docformatter/default.nix-
pkgs/development/python-modules/docformatter/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/docformatter/default.nix-    charset-normalizer
pkgs/development/python-modules/docformatter/default.nix-    tomli
pkgs/development/python-modules/docformatter/default.nix-    untokenize
--
pkgs/development/python-modules/rokuecp/default.nix-    aiohttp
pkgs/development/python-modules/rokuecp/default.nix-    backoff
pkgs/development/python-modules/rokuecp/default.nix-    cachetools
pkgs/development/python-modules/rokuecp/default.nix-    xmltodict
--
pkgs/development/python-modules/filedate/default.nix-    hash = "sha256-HvuGP+QlUlfAUfFmaVVvtPHGdrbWVxghQipnqTTvAQc=";
pkgs/development/python-modules/filedate/default.nix-  };
pkgs/development/python-modules/filedate/default.nix-
pkgs/development/python-modules/filedate/default.nix-  sourceRoot = "${src.name}/Files";
pkgs/development/python-modules/filedate/default.nix-
pkgs/development/python-modules/filedate/default.nix-  # The repo stores everything in "src" and uses setup.py to move "src" ->
pkgs/development/python-modules/filedate/default.nix-  # "filedate" before calling setup() and then tries to rename "filedate" back
pkgs/development/python-modules/filedate/default.nix-  # to "src" after.
pkgs/development/python-modules/filedate/default.nix-  postPatch = ''
pkgs/development/python-modules/filedate/default.nix-    mv src filedate
pkgs/development/python-modules/filedate/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/filedate/default.nix-      --replace-fail "__title__ = os.path.basename(os.path.dirname(os.path.dirname(__file__)))" '__title__ = "filedate"'
pkgs/development/python-modules/filedate/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/filedate/default.nix-      --replace-fail "cleanup = True" "cleanup = False"
pkgs/development/python-modules/filedate/default.nix-
pkgs/development/python-modules/filedate/default.nix-    # Disable renaming "filedate" dir back to "src"
--
pkgs/development/python-modules/cloudflare/default.nix-
pkgs/development/python-modules/cloudflare/default.nix-  disabled = pythonOlder "3.7";
pkgs/development/python-modules/cloudflare/default.nix-
pkgs/development/python-modules/cloudflare/default.nix-  src = fetchPypi {
pkgs/development/python-modules/cloudflare/default.nix-    inherit pname version;
pkgs/development/python-modules/cloudflare/default.nix-    hash = "sha256-seHGvuuNmPY7/gocuodPxOIuAAvMSQVE+VbGibO1slg=";
pkgs/development/python-modules/cloudflare/default.nix-  };
pkgs/development/python-modules/cloudflare/default.nix-
pkgs/development/python-modules/cloudflare/default.nix-  postPatch = ''
pkgs/development/python-modules/cloudflare/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/cloudflare/default.nix-      --replace-fail 'hatchling==1.26.3' 'hatchling>=1.26.3'
pkgs/development/python-modules/cloudflare/default.nix-  '';
pkgs/development/python-modules/cloudflare/default.nix-
pkgs/development/python-modules/cloudflare/default.nix-  build-system = [
pkgs/development/python-modules/cloudflare/default.nix-    hatchling
pkgs/development/python-modules/cloudflare/default.nix-    hatch-fancy-pypi-readme
pkgs/development/python-modules/cloudflare/default.nix-  ];
pkgs/development/python-modules/cloudflare/default.nix-
pkgs/development/python-modules/cloudflare/default.nix-  dependencies = [
pkgs/development/python-modules/cloudflare/default.nix-    httpx
--
--
pkgs/development/python-modules/qtile/default.nix-        --replace-fail /usr/include/libdrm ${lib.getDev libdrm}/include/libdrm
pkgs/development/python-modules/qtile/default.nix-  '';
pkgs/development/python-modules/qtile/default.nix-
pkgs/development/python-modules/qtile/default.nix-  build-system = [
pkgs/development/python-modules/qtile/default.nix-    setuptools
pkgs/development/python-modules/qtile/default.nix-    setuptools-scm
pkgs/development/python-modules/qtile/default.nix-    pkg-config
pkgs/development/python-modules/qtile/default.nix-  ];
pkgs/development/python-modules/qtile/default.nix-
--
pkgs/development/python-modules/markdown-macros/default.nix-    # Fixes a bug with markdown>2.4
pkgs/development/python-modules/markdown-macros/default.nix-    # https://github.com/wnielson/markdown-macros/pull/1
pkgs/development/python-modules/markdown-macros/default.nix-    (fetchpatch {
pkgs/development/python-modules/markdown-macros/default.nix-      name = "wnielson-markdown-macros-pull-1.patch";
pkgs/development/python-modules/markdown-macros/default.nix-      url = "https://github.com/wnielson/markdown-macros/commit/e38cba9acb6789cc128f6fe9ca427ba71815a20f.patch";
pkgs/development/python-modules/markdown-macros/default.nix-      sha256 = "17njbgq2srzkf03ar6yn92frnsbda3g45cdi529fdh0x8mmyxci0";
pkgs/development/python-modules/markdown-macros/default.nix-    })
pkgs/development/python-modules/markdown-macros/default.nix-  ];
pkgs/development/python-modules/markdown-macros/default.nix-
pkgs/development/python-modules/markdown-macros/default.nix-  prePatch = ''
pkgs/development/python-modules/markdown-macros/default.nix:    substituteInPlace setup.py --replace-fail "distribute" "setuptools"
--
pkgs/development/python-modules/oletools/default.nix-    msoffcrypto-tool
pkgs/development/python-modules/oletools/default.nix-    olefile
pkgs/development/python-modules/oletools/default.nix-    pcodedmp
pkgs/development/python-modules/oletools/default.nix-    pyparsing
pkgs/development/python-modules/oletools/default.nix-  ];
pkgs/development/python-modules/oletools/default.nix-
pkgs/development/python-modules/oletools/default.nix-  nativeCheckInputs = [ pytestCheckHook ];
pkgs/development/python-modules/oletools/default.nix-
pkgs/development/python-modules/oletools/default.nix-  postPatch = ''
pkgs/development/python-modules/oletools/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/oletools/default.nix-      --replace "pyparsing>=2.1.0,<3" "pyparsing>=2.1.0"
pkgs/development/python-modules/oletools/default.nix-  '';
pkgs/development/python-modules/oletools/default.nix-
pkgs/development/python-modules/oletools/default.nix-  disabledTests = [
pkgs/development/python-modules/oletools/default.nix-    # Test fails with AssertionError: Tuples differ: ('MS Word 2007+...
pkgs/development/python-modules/oletools/default.nix-    "test_all"
pkgs/development/python-modules/oletools/default.nix-    "test_xlm"
pkgs/development/python-modules/oletools/default.nix-  ];
pkgs/development/python-modules/oletools/default.nix-
pkgs/development/python-modules/oletools/default.nix-  pythonImportsCheck = [ "oletools" ];
--
--
pkgs/development/python-modules/gradient/default.nix-  version = "2.99.3";
pkgs/development/python-modules/gradient/default.nix-  format = "setuptools";
pkgs/development/python-modules/gradient/default.nix-
pkgs/development/python-modules/gradient/default.nix-  src = fetchPypi {
pkgs/development/python-modules/gradient/default.nix-    inherit pname version;
pkgs/development/python-modules/gradient/default.nix-    hash = "sha256-Ep3Qh9Q1xWt2JveCf/A/KInQ3cnGE7D1YNdavDS0ZE8=";
pkgs/development/python-modules/gradient/default.nix-  };
pkgs/development/python-modules/gradient/default.nix-
pkgs/development/python-modules/gradient/default.nix-  postPatch = ''
pkgs/development/python-modules/gradient/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/gradient/default.nix-      --replace 'attrs<=' 'attrs>=' \
pkgs/development/python-modules/gradient/default.nix-      --replace 'colorama==' 'colorama>=' \
pkgs/development/python-modules/gradient/default.nix-      --replace 'gql[requests]==3.0.0a6' 'gql' \
pkgs/development/python-modules/gradient/default.nix-      --replace 'PyYAML==5.*' 'PyYAML' \
pkgs/development/python-modules/gradient/default.nix-      --replace 'marshmallow<' 'marshmallow>=' \
pkgs/development/python-modules/gradient/default.nix-      --replace 'websocket-client==0.57.*' 'websocket-client'
pkgs/development/python-modules/gradient/default.nix-  '';
pkgs/development/python-modules/gradient/default.nix-
pkgs/development/python-modules/gradient/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/gradient/default.nix-    attrs
--
pkgs/development/python-modules/scs/default.nix-
pkgs/development/python-modules/scs/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/scs/default.nix-    owner = "bodono";
pkgs/development/python-modules/scs/default.nix-    repo = "scs-python";
pkgs/development/python-modules/scs/default.nix-    tag = version;
pkgs/development/python-modules/scs/default.nix-    fetchSubmodules = true;
pkgs/development/python-modules/scs/default.nix-    hash = "sha256-Dv0LDY6JFFq/dpcDsnU+ErnHJ8RDpaNhrRjEwY31Szk=";
pkgs/development/python-modules/scs/default.nix-  };
pkgs/development/python-modules/scs/default.nix-
pkgs/development/python-modules/scs/default.nix-  postPatch = ''
pkgs/development/python-modules/scs/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/scs/default.nix-      --replace-fail "numpy >= 2.0.0" "numpy"
pkgs/development/python-modules/scs/default.nix-  '';
pkgs/development/python-modules/scs/default.nix-
pkgs/development/python-modules/scs/default.nix-  build-system = [
pkgs/development/python-modules/scs/default.nix-    meson-python
pkgs/development/python-modules/scs/default.nix-    numpy
pkgs/development/python-modules/scs/default.nix-    pkg-config
pkgs/development/python-modules/scs/default.nix-  ];
pkgs/development/python-modules/scs/default.nix-
pkgs/development/python-modules/scs/default.nix-  buildInputs = lib.optionals (!stdenv.hostPlatform.isDarwin) [
--
--
pkgs/development/python-modules/odp-amsterdam/default.nix-    poetry-core
pkgs/development/python-modules/odp-amsterdam/default.nix-  ];
pkgs/development/python-modules/odp-amsterdam/default.nix-
pkgs/development/python-modules/odp-amsterdam/default.nix-  pythonRelaxDeps = [ "pytz" ];
pkgs/development/python-modules/odp-amsterdam/default.nix-
--
pkgs/development/python-modules/sanic-auth/default.nix-    sanic-testing
pkgs/development/python-modules/sanic-auth/default.nix-  ];
pkgs/development/python-modules/sanic-auth/default.nix-
pkgs/development/python-modules/sanic-auth/default.nix-  disabledTests = [
pkgs/development/python-modules/sanic-auth/default.nix-    # incompatible with sanic>=22.3.0
pkgs/development/python-modules/sanic-auth/default.nix-    "test_login_required"
pkgs/development/python-modules/sanic-auth/default.nix-  ];
pkgs/development/python-modules/sanic-auth/default.nix-
pkgs/development/python-modules/sanic-auth/default.nix-  postPatch = ''
pkgs/development/python-modules/sanic-auth/default.nix-    # Support for httpx>=0.20.0
pkgs/development/python-modules/sanic-auth/default.nix:    substituteInPlace tests/test_auth.py \
pkgs/development/python-modules/sanic-auth/default.nix-      --replace-fail "allow_redirects=False" "follow_redirects=False"
pkgs/development/python-modules/sanic-auth/default.nix-  '';
pkgs/development/python-modules/sanic-auth/default.nix-
pkgs/development/python-modules/sanic-auth/default.nix-  pythonImportsCheck = [ "sanic_auth" ];
pkgs/development/python-modules/sanic-auth/default.nix-
pkgs/development/python-modules/sanic-auth/default.nix-  meta = with lib; {
pkgs/development/python-modules/sanic-auth/default.nix-    description = "Simple Authentication for Sanic";
pkgs/development/python-modules/sanic-auth/default.nix-    homepage = "https://github.com/pyx/sanic-auth/";
pkgs/development/python-modules/sanic-auth/default.nix-    license = licenses.bsdOriginal;
--
pkgs/development/python-modules/wapiti-arsenic/default.nix-
pkgs/development/python-modules/wapiti-arsenic/default.nix-  # Latest tag is not on GitHub
pkgs/development/python-modules/wapiti-arsenic/default.nix-  src = fetchPypi {
pkgs/development/python-modules/wapiti-arsenic/default.nix-    pname = "wapiti_arsenic";
pkgs/development/python-modules/wapiti-arsenic/default.nix-    inherit version;
pkgs/development/python-modules/wapiti-arsenic/default.nix-    hash = "sha256-QxjM0BsiHm/LPUuGLLPG6OUcr4YXBEpfJGTwKp1zTWQ=";
pkgs/development/python-modules/wapiti-arsenic/default.nix-  };
pkgs/development/python-modules/wapiti-arsenic/default.nix-
pkgs/development/python-modules/wapiti-arsenic/default.nix-  postPatch = ''
pkgs/development/python-modules/wapiti-arsenic/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/wapiti-arsenic/default.nix-      --replace-fail "poetry>=0.12" "poetry-core" \
pkgs/development/python-modules/wapiti-arsenic/default.nix-      --replace-fail "poetry.masonry" "poetry.core.masonry"
pkgs/development/python-modules/wapiti-arsenic/default.nix-  '';
pkgs/development/python-modules/wapiti-arsenic/default.nix-
pkgs/development/python-modules/wapiti-arsenic/default.nix-  build-system = [
pkgs/development/python-modules/wapiti-arsenic/default.nix-    poetry-core
pkgs/development/python-modules/wapiti-arsenic/default.nix-  ];
pkgs/development/python-modules/wapiti-arsenic/default.nix-
pkgs/development/python-modules/wapiti-arsenic/default.nix-  pythonRelaxDeps = [
pkgs/development/python-modules/wapiti-arsenic/default.nix-    "structlog"
--
--
pkgs/development/python-modules/shaperglot/default.nix-    owner = "googlefonts";
pkgs/development/python-modules/shaperglot/default.nix-    repo = "shaperglot";
pkgs/development/python-modules/shaperglot/default.nix-    tag = "v${version}";
pkgs/development/python-modules/shaperglot/default.nix-    hash = "sha256-O6z7TJpC54QkqX5/G1HKSvaDYty7B9BnCQ4FpsLsEMs=";
pkgs/development/python-modules/shaperglot/default.nix-  };
pkgs/development/python-modules/shaperglot/default.nix-
pkgs/development/python-modules/shaperglot/default.nix-  env.PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION = "python";
pkgs/development/python-modules/shaperglot/default.nix-
pkgs/development/python-modules/shaperglot/default.nix-  postPatch = ''
pkgs/development/python-modules/shaperglot/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/shaperglot/default.nix-      --replace-fail "setuptools>=75.0.0" "setuptools"
pkgs/development/python-modules/shaperglot/default.nix-  '';
pkgs/development/python-modules/shaperglot/default.nix-
pkgs/development/python-modules/shaperglot/default.nix-  build-system = [
pkgs/development/python-modules/shaperglot/default.nix-    setuptools
pkgs/development/python-modules/shaperglot/default.nix-    setuptools-scm
pkgs/development/python-modules/shaperglot/default.nix-  ];
pkgs/development/python-modules/shaperglot/default.nix-
pkgs/development/python-modules/shaperglot/default.nix-  dependencies = [
pkgs/development/python-modules/shaperglot/default.nix-    gflanguages
--
--
pkgs/development/python-modules/pydelijn/default.nix-
pkgs/development/python-modules/pydelijn/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/pydelijn/default.nix-    aiohttp
pkgs/development/python-modules/pydelijn/default.nix-    async-timeout
pkgs/development/python-modules/pydelijn/default.nix-    pytz
pkgs/development/python-modules/pydelijn/default.nix-  ];
pkgs/development/python-modules/pydelijn/default.nix-
pkgs/development/python-modules/pydelijn/default.nix-  postPatch = ''
pkgs/development/python-modules/pydelijn/default.nix-    # Remove with next release
pkgs/development/python-modules/pydelijn/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/pydelijn/default.nix-      --replace "async_timeout>=3.0.1,<4.0" "async_timeout>=3.0.1"
pkgs/development/python-modules/pydelijn/default.nix-    # https://github.com/bollewolle/pydelijn/pull/11
pkgs/development/python-modules/pydelijn/default.nix:    substituteInPlace pydelijn/common.py \
pkgs/development/python-modules/pydelijn/default.nix-      --replace ", loop=self.loop" ""
pkgs/development/python-modules/pydelijn/default.nix-  '';
pkgs/development/python-modules/pydelijn/default.nix-
pkgs/development/python-modules/pydelijn/default.nix-  # Project has no tests
pkgs/development/python-modules/pydelijn/default.nix-  doCheck = false;
pkgs/development/python-modules/pydelijn/default.nix-
pkgs/development/python-modules/pydelijn/default.nix-  pythonImportsCheck = [ "pydelijn" ];
pkgs/development/python-modules/pydelijn/default.nix-
--
pkgs/development/python-modules/dbus-fast/default.nix-
pkgs/development/python-modules/dbus-fast/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/dbus-fast/default.nix-    owner = "Bluetooth-Devices";
pkgs/development/python-modules/dbus-fast/default.nix-    repo = "dbus-fast";
pkgs/development/python-modules/dbus-fast/default.nix-    tag = "v${version}";
pkgs/development/python-modules/dbus-fast/default.nix-    hash = "sha256-ZpTQjAmrLoenDWzd/0NpD7fqTd6Dv1J0Ks0db4twwYk=";
pkgs/development/python-modules/dbus-fast/default.nix-  };
pkgs/development/python-modules/dbus-fast/default.nix-
pkgs/development/python-modules/dbus-fast/default.nix-  postPatch = ''
pkgs/development/python-modules/dbus-fast/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/dbus-fast/default.nix-      --replace-fail "Cython>=3,<3.1.0" Cython
pkgs/development/python-modules/dbus-fast/default.nix-  '';
pkgs/development/python-modules/dbus-fast/default.nix-
pkgs/development/python-modules/dbus-fast/default.nix-  # The project can build both an optimized cython version and an unoptimized
pkgs/development/python-modules/dbus-fast/default.nix-  # python version. This ensures we fail if we build the wrong one.
pkgs/development/python-modules/dbus-fast/default.nix-  env.REQUIRE_CYTHON = 1;
pkgs/development/python-modules/dbus-fast/default.nix-
pkgs/development/python-modules/dbus-fast/default.nix-  build-system = [
pkgs/development/python-modules/dbus-fast/default.nix-    cython
pkgs/development/python-modules/dbus-fast/default.nix-    poetry-core
--
--
pkgs/development/python-modules/withings-api/default.nix-
pkgs/development/python-modules/withings-api/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/withings-api/default.nix-    owner = "vangorra";
pkgs/development/python-modules/withings-api/default.nix-    repo = "python_withings_api";
pkgs/development/python-modules/withings-api/default.nix-    tag = version;
pkgs/development/python-modules/withings-api/default.nix-    hash = "sha256-8cOLHYnodPGk1b1n6xbVyW2iju3cG6MgnzYTKDsP/nw=";
pkgs/development/python-modules/withings-api/default.nix-  };
pkgs/development/python-modules/withings-api/default.nix-
pkgs/development/python-modules/withings-api/default.nix-  postPatch = ''
pkgs/development/python-modules/withings-api/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/withings-api/default.nix-      --replace-fail 'requests-oauth = ">=0.4.1"' '''
pkgs/development/python-modules/withings-api/default.nix-  '';
pkgs/development/python-modules/withings-api/default.nix-
pkgs/development/python-modules/withings-api/default.nix-  build-system = [ poetry-core ];
pkgs/development/python-modules/withings-api/default.nix-
pkgs/development/python-modules/withings-api/default.nix-  dependencies = [
pkgs/development/python-modules/withings-api/default.nix-    arrow
pkgs/development/python-modules/withings-api/default.nix-    requests-oauthlib
pkgs/development/python-modules/withings-api/default.nix-    typing-extensions
pkgs/development/python-modules/withings-api/default.nix-    pydantic
--
--
pkgs/development/python-modules/pywal/default.nix-    mainProgram = "wal";
pkgs/development/python-modules/pywal/default.nix-    homepage = "https://github.com/dylanaraps/pywal";
pkgs/development/python-modules/pywal/default.nix-    license = licenses.mit;
pkgs/development/python-modules/pywal/default.nix-    maintainers = with maintainers; [ Fresheyeball ];
--
pkgs/development/python-modules/pyqt/6.x.nix-  ];
pkgs/development/python-modules/pyqt/6.x.nix-
pkgs/development/python-modules/pyqt/6.x.nix-  # be more verbose
pkgs/development/python-modules/pyqt/6.x.nix-  # and normalize version
pkgs/development/python-modules/pyqt/6.x.nix-  postPatch = ''
pkgs/development/python-modules/pyqt/6.x.nix-    cat >> pyproject.toml <<EOF
pkgs/development/python-modules/pyqt/6.x.nix-    [tool.sip.project]
pkgs/development/python-modules/pyqt/6.x.nix-    verbose = true
pkgs/development/python-modules/pyqt/6.x.nix-    EOF
pkgs/development/python-modules/pyqt/6.x.nix-
pkgs/development/python-modules/pyqt/6.x.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/pyqt/6.x.nix-      --replace-fail 'version = "${version}"' 'version = "${lib.versions.pad 3 version}"'
pkgs/development/python-modules/pyqt/6.x.nix-  '';
pkgs/development/python-modules/pyqt/6.x.nix-
pkgs/development/python-modules/pyqt/6.x.nix-  enableParallelBuilding = true;
pkgs/development/python-modules/pyqt/6.x.nix-  # HACK: paralellize compilation of make calls within pyqt's setup.py
--
pkgs/development/python-modules/django-pgpubsub/default.nix-    repo = "django-pgpubsub";
pkgs/development/python-modules/django-pgpubsub/default.nix-    tag = version;
pkgs/development/python-modules/django-pgpubsub/default.nix-    hash = "sha256-Gl6NfBaoj3WKLHwJElbb27CYVQ83s3f86NUOZE7lHCk=";
pkgs/development/python-modules/django-pgpubsub/default.nix-  };
pkgs/development/python-modules/django-pgpubsub/default.nix-
pkgs/development/python-modules/django-pgpubsub/default.nix-  passthru.updateScript = nix-update-script { };
pkgs/development/python-modules/django-pgpubsub/default.nix-
pkgs/development/python-modules/django-pgpubsub/default.nix-  postPatch = ''
pkgs/development/python-modules/django-pgpubsub/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/django-pgpubsub/default.nix-    --replace 'poetry.masonry.api' 'poetry.core.masonry.api' \
pkgs/development/python-modules/django-pgpubsub/default.nix-    --replace 'poetry>=1.1.13' 'poetry-core>=1.0.0' \
pkgs/development/python-modules/django-pgpubsub/default.nix-  '';
pkgs/development/python-modules/django-pgpubsub/default.nix-
pkgs/development/python-modules/django-pgpubsub/default.nix-  build-system = [ poetry-core ];
pkgs/development/python-modules/django-pgpubsub/default.nix-
pkgs/development/python-modules/django-pgpubsub/default.nix-  dependencies = [
pkgs/development/python-modules/django-pgpubsub/default.nix-    django
pkgs/development/python-modules/django-pgpubsub/default.nix-    django-pgtrigger
pkgs/development/python-modules/django-pgpubsub/default.nix-  ];
--
pkgs/development/python-modules/datrie/default.nix-  pname = "datrie";
--
pkgs/development/python-modules/thingspeak/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/thingspeak/default.nix-    owner = "mchwalisz";
pkgs/development/python-modules/thingspeak/default.nix-    repo = "thingspeak";
pkgs/development/python-modules/thingspeak/default.nix-    tag = "v${version}";
pkgs/development/python-modules/thingspeak/default.nix-    hash = "sha256-9YvudzksWp130hkG8WxiX9WHegAVH2TT1vwMbLJ13qE=";
pkgs/development/python-modules/thingspeak/default.nix-  };
pkgs/development/python-modules/thingspeak/default.nix-
pkgs/development/python-modules/thingspeak/default.nix-  postPatch = ''
pkgs/development/python-modules/thingspeak/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/thingspeak/default.nix-      --replace-fail "poetry.masonry.api" "poetry.core.masonry.api" \
pkgs/development/python-modules/thingspeak/default.nix-      --replace-fail 'requires = ["poetry>=0.12"]' 'requires = ["poetry-core"]'
pkgs/development/python-modules/thingspeak/default.nix-  '';
pkgs/development/python-modules/thingspeak/default.nix-
pkgs/development/python-modules/thingspeak/default.nix-  build-system = [
pkgs/development/python-modules/thingspeak/default.nix-    poetry-core
pkgs/development/python-modules/thingspeak/default.nix-  ];
pkgs/development/python-modules/thingspeak/default.nix-
pkgs/development/python-modules/thingspeak/default.nix-  dependencies = [
pkgs/development/python-modules/thingspeak/default.nix-    docopt
--
pkgs/development/python-modules/dask/default.nix-    owner = "dask";
pkgs/development/python-modules/dask/default.nix-    repo = "dask";
pkgs/development/python-modules/dask/default.nix-    tag = version;
pkgs/development/python-modules/dask/default.nix-    hash = "sha256-bwM4Q95YTEp9pDz6LmBLOeYjmi8nH8Cc/srZlXfEIlg=";
pkgs/development/python-modules/dask/default.nix-  };
pkgs/development/python-modules/dask/default.nix-
pkgs/development/python-modules/dask/default.nix-  postPatch = ''
pkgs/development/python-modules/dask/default.nix-    # versioneer hack to set version of GitHub package
pkgs/development/python-modules/dask/default.nix-    echo "def get_versions(): return {'dirty': False, 'error': None, 'full-revisionid': None, 'version': '${version}'}" > dask/_version.py
pkgs/development/python-modules/dask/default.nix-
pkgs/development/python-modules/dask/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/dask/default.nix-      --replace-fail "import versioneer" "" \
pkgs/development/python-modules/dask/default.nix-      --replace-fail "version=versioneer.get_version()," "version='${version}'," \
pkgs/development/python-modules/dask/default.nix-      --replace-fail "cmdclass=versioneer.get_cmdclass()," ""
pkgs/development/python-modules/dask/default.nix-
pkgs/development/python-modules/dask/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/dask/default.nix-      --replace-fail ', "versioneer[toml]==0.29"' ""
pkgs/development/python-modules/dask/default.nix-  '';
pkgs/development/python-modules/dask/default.nix-
--
pkgs/development/python-modules/explorerscript/default.nix-    owner = "SkyTemple";
pkgs/development/python-modules/explorerscript/default.nix-    repo = "explorerscript";
pkgs/development/python-modules/explorerscript/default.nix-    tag = version;
pkgs/development/python-modules/explorerscript/default.nix-    hash = "sha256-fh40HCU12AVA3cZ5xvRott+93qo8VzHFsbPzTkoV3x4=";
pkgs/development/python-modules/explorerscript/default.nix-    # Include a pinned antlr4 fork used as a C++ library
pkgs/development/python-modules/explorerscript/default.nix-    fetchSubmodules = true;
pkgs/development/python-modules/explorerscript/default.nix-  };
pkgs/development/python-modules/explorerscript/default.nix-
pkgs/development/python-modules/explorerscript/default.nix-  postPatch = ''
pkgs/development/python-modules/explorerscript/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/explorerscript/default.nix-      --replace-fail "scikit-build-core>=0.10.7, < 0.11" "scikit-build-core"
pkgs/development/python-modules/explorerscript/default.nix-  '';
pkgs/development/python-modules/explorerscript/default.nix-
pkgs/development/python-modules/explorerscript/default.nix-  build-system = [
pkgs/development/python-modules/explorerscript/default.nix-    setuptools
pkgs/development/python-modules/explorerscript/default.nix-    scikit-build-core
pkgs/development/python-modules/explorerscript/default.nix-    pybind11
pkgs/development/python-modules/explorerscript/default.nix-  ];
pkgs/development/python-modules/explorerscript/default.nix-
pkgs/development/python-modules/explorerscript/default.nix-  nativeBuildInputs = [
--
--
pkgs/development/python-modules/nbtlib/default.nix-
pkgs/development/python-modules/nbtlib/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/nbtlib/default.nix-    owner = "vberlier";
pkgs/development/python-modules/nbtlib/default.nix-    repo = "nbtlib";
pkgs/development/python-modules/nbtlib/default.nix-    rev = "v${version}";
pkgs/development/python-modules/nbtlib/default.nix-    hash = "sha256-L8eX6/0qiQ4UxbmDicLedzj+oBjYmlK96NpljE/A3eI=";
pkgs/development/python-modules/nbtlib/default.nix-  };
pkgs/development/python-modules/nbtlib/default.nix-
pkgs/development/python-modules/nbtlib/default.nix-  prePatch = ''
pkgs/development/python-modules/nbtlib/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/nbtlib/default.nix-    --replace "poetry>=0.12" "poetry-core" \
pkgs/development/python-modules/nbtlib/default.nix-    --replace "poetry.masonry" "poetry.core.masonry"
pkgs/development/python-modules/nbtlib/default.nix-  '';
pkgs/development/python-modules/nbtlib/default.nix-
pkgs/development/python-modules/nbtlib/default.nix-  nativeBuildInputs = [ poetry-core ];
pkgs/development/python-modules/nbtlib/default.nix-
pkgs/development/python-modules/nbtlib/default.nix-  propagatedBuildInputs = [ numpy ];
pkgs/development/python-modules/nbtlib/default.nix-
pkgs/development/python-modules/nbtlib/default.nix-  pythonImportsCheck = [ "nbtlib" ];
pkgs/development/python-modules/nbtlib/default.nix-
--
--
pkgs/development/python-modules/plotille/default.nix-    (fetchpatch {
pkgs/development/python-modules/plotille/default.nix-      name = "add-build-information";
pkgs/development/python-modules/plotille/default.nix-      url = "https://github.com/tammoippen/plotille/commit/db744e1fa9c141290966476ddf22a5e7d9a00c0a.patch";
pkgs/development/python-modules/plotille/default.nix-      hash = "sha256-8vBVKrcH7R1d9ol3D7RLVtAzZbpMsB9rA1KHD7t3Ydc=";
pkgs/development/python-modules/plotille/default.nix-    })
pkgs/development/python-modules/plotille/default.nix-  ];
pkgs/development/python-modules/plotille/default.nix-
pkgs/development/python-modules/plotille/default.nix-  postPatch = ''
pkgs/development/python-modules/plotille/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/plotille/default.nix-      --replace-fail poetry.masonry.api poetry.core.masonry.api \
pkgs/development/python-modules/plotille/default.nix-      --replace-fail "poetry>=" "poetry-core>="
pkgs/development/python-modules/plotille/default.nix-  '';
pkgs/development/python-modules/plotille/default.nix-
pkgs/development/python-modules/plotille/default.nix-  build-system = [
pkgs/development/python-modules/plotille/default.nix-    poetry-core
pkgs/development/python-modules/plotille/default.nix-    setuptools
pkgs/development/python-modules/plotille/default.nix-  ];
pkgs/development/python-modules/plotille/default.nix-
pkgs/development/python-modules/plotille/default.nix-  pythonImportsCheck = [
--
pkgs/development/python-modules/ffmpy/default.nix-  src = fetchFromGitHub {
--
pkgs/development/python-modules/ffmpy/default.nix-    # Default to store ffmpeg.
pkgs/development/python-modules/ffmpy/default.nix-    ''
pkgs/development/python-modules/ffmpy/default.nix:      substituteInPlace ffmpy/ffmpy.py \
pkgs/development/python-modules/ffmpy/default.nix-        --replace-fail \
pkgs/development/python-modules/ffmpy/default.nix-          'executable: str = "ffmpeg",' \
pkgs/development/python-modules/ffmpy/default.nix-          'executable: str = "${lib.getExe ffmpeg-headless}",'
pkgs/development/python-modules/ffmpy/default.nix-    ''
pkgs/development/python-modules/ffmpy/default.nix-    # The tests test a mock that does not behave like ffmpeg. If we default to the nix-store ffmpeg they fail.
pkgs/development/python-modules/ffmpy/default.nix-    + ''
pkgs/development/python-modules/ffmpy/default.nix-      for fname in tests/*.py; do
pkgs/development/python-modules/ffmpy/default.nix-        echo >>"$fname" 'FFmpeg.__init__.__defaults__ = ("ffmpeg", *FFmpeg.__init__.__defaults__[1:])'
pkgs/development/python-modules/ffmpy/default.nix-      done
pkgs/development/python-modules/ffmpy/default.nix-    '';
--
pkgs/development/python-modules/libarchive-c/default.nix-    # https://github.com/Changaco/python-libarchive-c/pull/141
pkgs/development/python-modules/libarchive-c/default.nix-    (fetchpatch {
pkgs/development/python-modules/libarchive-c/default.nix-      url = "https://github.com/Changaco/python-libarchive-c/commit/e0e2a47b2403632642ee932dd56acd11e4a79efe.diff";
pkgs/development/python-modules/libarchive-c/default.nix-      hash = "sha256-C9eD4cGQOIdBYy4ytom49lA/Jaarj7LbSIgjxCk/H84=";
pkgs/development/python-modules/libarchive-c/default.nix-    })
pkgs/development/python-modules/libarchive-c/default.nix-  ];
pkgs/development/python-modules/libarchive-c/default.nix-
--
pkgs/development/python-modules/mrsqm/default.nix-    pandas
pkgs/development/python-modules/mrsqm/default.nix-    scikit-learn
pkgs/development/python-modules/mrsqm/default.nix-    numpy
pkgs/development/python-modules/mrsqm/default.nix-    pip
pkgs/development/python-modules/mrsqm/default.nix-  ];
pkgs/development/python-modules/mrsqm/default.nix-
pkgs/development/python-modules/mrsqm/default.nix-  postPatch = ''
pkgs/development/python-modules/mrsqm/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/mrsqm/default.nix-      --replace-fail "setup_requires=['pytest-runner']," ""
pkgs/development/python-modules/mrsqm/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/mrsqm/default.nix-      --replace-fail "numpy==" "numpy>="
pkgs/development/python-modules/mrsqm/default.nix-  '';
pkgs/development/python-modules/mrsqm/default.nix-
pkgs/development/python-modules/mrsqm/default.nix-  preBuild = ''
pkgs/development/python-modules/mrsqm/default.nix-    export HOME=$(mktemp -d)
pkgs/development/python-modules/mrsqm/default.nix-  '';
pkgs/development/python-modules/mrsqm/default.nix-
pkgs/development/python-modules/mrsqm/default.nix-  nativeCheckInputs = [
pkgs/development/python-modules/mrsqm/default.nix-    pytestCheckHook
pkgs/development/python-modules/mrsqm/default.nix-  ];
--
--
pkgs/development/python-modules/dictdiffer/default.nix-    rev = "v${version}";
pkgs/development/python-modules/dictdiffer/default.nix-    hash = "sha256-lQyPs3lQWtsvNPuvvwJUTDzrFaOX5uwGuRHe3yWUheU=";
pkgs/development/python-modules/dictdiffer/default.nix-  };
pkgs/development/python-modules/dictdiffer/default.nix-
pkgs/development/python-modules/dictdiffer/default.nix-  nativeBuildInputs = [ setuptools-scm ];
pkgs/development/python-modules/dictdiffer/default.nix-
pkgs/development/python-modules/dictdiffer/default.nix-  nativeCheckInputs = [ pytestCheckHook ];
pkgs/development/python-modules/dictdiffer/default.nix-
pkgs/development/python-modules/dictdiffer/default.nix-  postPatch = ''
pkgs/development/python-modules/dictdiffer/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/dictdiffer/default.nix-      --replace "'pytest-runner>=2.7'," ""
pkgs/development/python-modules/dictdiffer/default.nix:    substituteInPlace pytest.ini \
pkgs/development/python-modules/dictdiffer/default.nix-      --replace ' --isort --pydocstyle --pycodestyle --doctest-glob="*.rst" --doctest-modules --cov=dictdiffer --cov-report=term-missing' ""
pkgs/development/python-modules/dictdiffer/default.nix-  '';
pkgs/development/python-modules/dictdiffer/default.nix-
pkgs/development/python-modules/dictdiffer/default.nix-  pythonImportsCheck = [ "dictdiffer" ];
pkgs/development/python-modules/dictdiffer/default.nix-
pkgs/development/python-modules/dictdiffer/default.nix-  meta = with lib; {
pkgs/development/python-modules/dictdiffer/default.nix-    description = "Module to diff and patch dictionaries";
pkgs/development/python-modules/dictdiffer/default.nix-    homepage = "https://github.com/inveniosoftware/dictdiffer";
pkgs/development/python-modules/dictdiffer/default.nix-    license = licenses.mit;
--
pkgs/development/python-modules/publicsuffix2/default.nix-    repo = "python-publicsuffix2";
pkgs/development/python-modules/publicsuffix2/default.nix-    rev = "release-${tagVersion}";
pkgs/development/python-modules/publicsuffix2/default.nix-    hash = "sha256-OV0O4LLxQ2LQiEHc1JTvScu35o2IWxo/hgn/COh2e7Y=";
pkgs/development/python-modules/publicsuffix2/default.nix-  };
pkgs/development/python-modules/publicsuffix2/default.nix-
pkgs/development/python-modules/publicsuffix2/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/publicsuffix2/default.nix-
pkgs/development/python-modules/publicsuffix2/default.nix-  postPatch = ''
pkgs/development/python-modules/publicsuffix2/default.nix-    # only used to update the interal publicsuffix list
pkgs/development/python-modules/publicsuffix2/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/publicsuffix2/default.nix-      --replace "'requests >= 2.7.0'," ""
pkgs/development/python-modules/publicsuffix2/default.nix-  '';
pkgs/development/python-modules/publicsuffix2/default.nix-
pkgs/development/python-modules/publicsuffix2/default.nix-  pythonImportsCheck = [ "publicsuffix2" ];
pkgs/development/python-modules/publicsuffix2/default.nix-
pkgs/development/python-modules/publicsuffix2/default.nix-  meta = with lib; {
pkgs/development/python-modules/publicsuffix2/default.nix-    description = "Get a public suffix for a domain name using the Public Suffix List";
pkgs/development/python-modules/publicsuffix2/default.nix-    homepage = "https://github.com/nexB/python-publicsuffix2";
pkgs/development/python-modules/publicsuffix2/default.nix-    license = licenses.mpl20;
pkgs/development/python-modules/publicsuffix2/default.nix-    maintainers = [ ];
--
--
pkgs/development/python-modules/pytest-playwright/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/pytest-playwright/default.nix-    owner = "microsoft";
pkgs/development/python-modules/pytest-playwright/default.nix-    repo = "playwright-pytest";
pkgs/development/python-modules/pytest-playwright/default.nix-    tag = "v${version}";
pkgs/development/python-modules/pytest-playwright/default.nix-    hash = "sha256-GcvasyCVNUWieIYj7Da5dWdXtxVAhP2lR+ogBzrBu4M=";
pkgs/development/python-modules/pytest-playwright/default.nix-  };
pkgs/development/python-modules/pytest-playwright/default.nix-
pkgs/development/python-modules/pytest-playwright/default.nix-  postPatch = ''
pkgs/development/python-modules/pytest-playwright/default.nix-    pushd pytest-playwright
pkgs/development/python-modules/pytest-playwright/default.nix-
pkgs/development/python-modules/pytest-playwright/default.nix:    substituteInPlace pyproject.toml --replace-fail "==" ">="
pkgs/development/python-modules/pytest-playwright/default.nix-  '';
pkgs/development/python-modules/pytest-playwright/default.nix-
pkgs/development/python-modules/pytest-playwright/default.nix-  build-system = [
pkgs/development/python-modules/pytest-playwright/default.nix-    setuptools
pkgs/development/python-modules/pytest-playwright/default.nix-    setuptools-scm
pkgs/development/python-modules/pytest-playwright/default.nix-  ];
pkgs/development/python-modules/pytest-playwright/default.nix-
pkgs/development/python-modules/pytest-playwright/default.nix-  buildInputs = [ pytest ];
pkgs/development/python-modules/pytest-playwright/default.nix-
pkgs/development/python-modules/pytest-playwright/default.nix-  dependencies = [
--
pkgs/development/python-modules/ducc0/default.nix-
pkgs/development/python-modules/ducc0/default.nix-  src = fetchFromGitLab {
pkgs/development/python-modules/ducc0/default.nix-    domain = "gitlab.mpcdf.mpg.de";
pkgs/development/python-modules/ducc0/default.nix-    owner = "mtr";
pkgs/development/python-modules/ducc0/default.nix-    repo = "ducc";
pkgs/development/python-modules/ducc0/default.nix-    tag = "ducc0_${lib.replaceStrings [ "." ] [ "_" ] version}";
pkgs/development/python-modules/ducc0/default.nix-    hash = "sha256-Be7lw9i1uEOY3w/Efnn7sZ4Xg5DenQuih6uReCmOI1I=";
pkgs/development/python-modules/ducc0/default.nix-  };
pkgs/development/python-modules/ducc0/default.nix-
pkgs/development/python-modules/ducc0/default.nix-  postPatch = ''
pkgs/development/python-modules/ducc0/default.nix:    substituteInPlace pyproject.toml --replace-fail '"pybind11>=2.13.6", ' ""
pkgs/development/python-modules/ducc0/default.nix-  '';
pkgs/development/python-modules/ducc0/default.nix-
pkgs/development/python-modules/ducc0/default.nix-  DUCC0_USE_NANOBIND = "";
pkgs/development/python-modules/ducc0/default.nix-  DUCC0_OPTIMIZATION = "portable";
pkgs/development/python-modules/ducc0/default.nix-
pkgs/development/python-modules/ducc0/default.nix-  build-system = [
pkgs/development/python-modules/ducc0/default.nix-    cmake
pkgs/development/python-modules/ducc0/default.nix-    nanobind
pkgs/development/python-modules/ducc0/default.nix-    ninja
pkgs/development/python-modules/ducc0/default.nix-    scikit-build-core
--
pkgs/development/python-modules/raincloudy/default.nix-    # fix raincloudy.aio package discovery, by relying on
pkgs/development/python-modules/raincloudy/default.nix-    # autodiscovery instead.
pkgs/development/python-modules/raincloudy/default.nix-    sed -i '/packages=/d' setup.py
pkgs/development/python-modules/raincloudy/default.nix-  '';
pkgs/development/python-modules/raincloudy/default.nix-
pkgs/development/python-modules/raincloudy/default.nix-  build-system = [
pkgs/development/python-modules/raincloudy/default.nix-    setuptools
pkgs/development/python-modules/raincloudy/default.nix-    setuptools-scm
--
pkgs/development/python-modules/wacz/default.nix-  patches = [
pkgs/development/python-modules/wacz/default.nix-    # <https://github.com/webrecorder/py-wacz/pull/47>
pkgs/development/python-modules/wacz/default.nix-    (fetchpatch {
pkgs/development/python-modules/wacz/default.nix-      name = "clean-up-deps.patch";
pkgs/development/python-modules/wacz/default.nix-      url = "https://github.com/webrecorder/py-wacz/compare/1e8f724a527f28855eedeb0d969ee39b00b2a80a...9d3ad60f125247b8a4354511d9123b85ce6a23c5.patch";
pkgs/development/python-modules/wacz/default.nix-      hash = "sha256-zH6BKhsq9ybjzaWcNbVkk1sWh8vVCkv7Qxuwl0MQhNM=";
pkgs/development/python-modules/wacz/default.nix-    })
pkgs/development/python-modules/wacz/default.nix-  ];
pkgs/development/python-modules/wacz/default.nix-
pkgs/development/python-modules/wacz/default.nix-  postPatch = ''
pkgs/development/python-modules/wacz/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/wacz/default.nix-      --replace "pytest-runner" ""
--
pkgs/development/python-modules/monotonic/default.nix-  };
pkgs/development/python-modules/monotonic/default.nix-
pkgs/development/python-modules/monotonic/default.nix-  __propagatedImpureHostDeps = lib.optional stdenv.hostPlatform.isDarwin "/usr/lib/libc.dylib";
pkgs/development/python-modules/monotonic/default.nix-
pkgs/development/python-modules/monotonic/default.nix-  patchPhase = lib.optionalString stdenv.hostPlatform.isLinux ''
pkgs/development/python-modules/monotonic/default.nix:    substituteInPlace monotonic.py --replace \
pkgs/development/python-modules/monotonic/default.nix-      "ctypes.util.find_library('c')" "'${stdenv.cc.libc}/lib/libc.so'"
pkgs/development/python-modules/monotonic/default.nix-  '';
pkgs/development/python-modules/monotonic/default.nix-
pkgs/development/python-modules/monotonic/default.nix-  meta = with lib; {
pkgs/development/python-modules/monotonic/default.nix-    description = "Implementation of time.monotonic() for Python 2 & < 3.3";
pkgs/development/python-modules/monotonic/default.nix-    homepage = "https://github.com/atdt/monotonic";
pkgs/development/python-modules/monotonic/default.nix-    license = licenses.asl20;
pkgs/development/python-modules/monotonic/default.nix-  };
pkgs/development/python-modules/monotonic/default.nix-}
--
pkgs/development/python-modules/arch/default.nix-  pyproject = true;
pkgs/development/python-modules/arch/default.nix-
pkgs/development/python-modules/arch/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/arch/default.nix-    owner = "bashtage";
pkgs/development/python-modules/arch/default.nix-    repo = "arch";
--
pkgs/development/python-modules/py-cpuinfo/default.nix-    repo = "py-cpuinfo";
pkgs/development/python-modules/py-cpuinfo/default.nix-    rev = "v${version}";
pkgs/development/python-modules/py-cpuinfo/default.nix-    hash = "sha256-Q5u0guAqDVhf6bvJTzNvCpWbIzjxxAjE7s0OuXj9T4Q=";
pkgs/development/python-modules/py-cpuinfo/default.nix-  };
pkgs/development/python-modules/py-cpuinfo/default.nix-
pkgs/development/python-modules/py-cpuinfo/default.nix-  nativeCheckInputs = [ pytestCheckHook ];
pkgs/development/python-modules/py-cpuinfo/default.nix-
pkgs/development/python-modules/py-cpuinfo/default.nix-  # On Darwin sysctl is used to read CPU information.
pkgs/development/python-modules/py-cpuinfo/default.nix-  postPatch = lib.optionalString stdenv.hostPlatform.isDarwin ''
pkgs/development/python-modules/py-cpuinfo/default.nix:    substituteInPlace cpuinfo/cpuinfo.py \
pkgs/development/python-modules/py-cpuinfo/default.nix-      --replace "len(_program_paths('sysctl')) > 0" "True" \
pkgs/development/python-modules/py-cpuinfo/default.nix-      --replace "_run_and_get_stdout(['sysctl'" "_run_and_get_stdout(['${sysctl}/bin/sysctl'"
pkgs/development/python-modules/py-cpuinfo/default.nix-  '';
pkgs/development/python-modules/py-cpuinfo/default.nix-
pkgs/development/python-modules/py-cpuinfo/default.nix-  pythonImportsCheck = [ "cpuinfo" ];
pkgs/development/python-modules/py-cpuinfo/default.nix-
pkgs/development/python-modules/py-cpuinfo/default.nix-  meta = with lib; {
pkgs/development/python-modules/py-cpuinfo/default.nix-    description = "Get CPU info with pure Python";
pkgs/development/python-modules/py-cpuinfo/default.nix-    mainProgram = "cpuinfo";
pkgs/development/python-modules/py-cpuinfo/default.nix-    longDescription = ''
--
--
pkgs/development/python-modules/systembridgeconnector/default.nix-
pkgs/development/python-modules/systembridgeconnector/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/systembridgeconnector/default.nix-    owner = "timmo001";
pkgs/development/python-modules/systembridgeconnector/default.nix-    repo = "system-bridge-connector";
pkgs/development/python-modules/systembridgeconnector/default.nix-    tag = version;
pkgs/development/python-modules/systembridgeconnector/default.nix-    hash = "sha256-E04ETXfrh+1OY8WsNNJEeYlnqQcHWR3CX/E7SOd7/24=";
pkgs/development/python-modules/systembridgeconnector/default.nix-  };
pkgs/development/python-modules/systembridgeconnector/default.nix-
pkgs/development/python-modules/systembridgeconnector/default.nix-  postPatch = ''
pkgs/development/python-modules/systembridgeconnector/default.nix:    substituteInPlace requirements_setup.txt \
pkgs/development/python-modules/systembridgeconnector/default.nix-      --replace-fail ">=" " #"
pkgs/development/python-modules/systembridgeconnector/default.nix-
pkgs/development/python-modules/systembridgeconnector/default.nix:    substituteInPlace systembridgeconnector/_version.py \
pkgs/development/python-modules/systembridgeconnector/default.nix-      --replace-fail ", dev=0" ""
pkgs/development/python-modules/systembridgeconnector/default.nix-  '';
pkgs/development/python-modules/systembridgeconnector/default.nix-
pkgs/development/python-modules/systembridgeconnector/default.nix-  build-system = [
pkgs/development/python-modules/systembridgeconnector/default.nix-    incremental
pkgs/development/python-modules/systembridgeconnector/default.nix-    setuptools
pkgs/development/python-modules/systembridgeconnector/default.nix-  ];
pkgs/development/python-modules/systembridgeconnector/default.nix-
--
pkgs/development/python-modules/persistent/default.nix-
pkgs/development/python-modules/persistent/default.nix-  disabled = pythonOlder "3.7";
pkgs/development/python-modules/persistent/default.nix-
pkgs/development/python-modules/persistent/default.nix-  src = fetchPypi {
pkgs/development/python-modules/persistent/default.nix-    inherit pname version;
pkgs/development/python-modules/persistent/default.nix-    hash = "sha256-LTIbYOsH75APhals8HH/jDua7m5nm+zEjEbzRX6NnS8=";
pkgs/development/python-modules/persistent/default.nix-  };
pkgs/development/python-modules/persistent/default.nix-
pkgs/development/python-modules/persistent/default.nix-  postPatch = ''
pkgs/development/python-modules/persistent/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/persistent/default.nix-      --replace-fail "setuptools < 74" "setuptools"
pkgs/development/python-modules/persistent/default.nix-  '';
pkgs/development/python-modules/persistent/default.nix-
pkgs/development/python-modules/persistent/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/persistent/default.nix-
pkgs/development/python-modules/persistent/default.nix-  dependencies = [
pkgs/development/python-modules/persistent/default.nix-    zope-interface
pkgs/development/python-modules/persistent/default.nix-    zope-deferredimport
pkgs/development/python-modules/persistent/default.nix-  ]
pkgs/development/python-modules/persistent/default.nix-  ++ lib.optionals (!isPyPy) [ cffi ];
--
--
pkgs/development/python-modules/zigpy-znp/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/zigpy-znp/default.nix-    owner = "zigpy";
pkgs/development/python-modules/zigpy-znp/default.nix-    repo = "zigpy-znp";
pkgs/development/python-modules/zigpy-znp/default.nix-    tag = "v${version}";
pkgs/development/python-modules/zigpy-znp/default.nix-    hash = "sha256-V662zDUBMbr+cARxrwt8196Ml4zlGEAudR3BtvY96HM=";
pkgs/development/python-modules/zigpy-znp/default.nix-  };
pkgs/development/python-modules/zigpy-znp/default.nix-
pkgs/development/python-modules/zigpy-znp/default.nix-  postPatch = ''
pkgs/development/python-modules/zigpy-znp/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/zigpy-znp/default.nix-      --replace-fail "timeout = 20" "timeout = 300" \
pkgs/development/python-modules/zigpy-znp/default.nix-      --replace-fail ', "setuptools-git-versioning<2"' "" \
pkgs/development/python-modules/zigpy-znp/default.nix-      --replace-fail 'dynamic = ["version"]' 'version = "${version}"'
pkgs/development/python-modules/zigpy-znp/default.nix-  '';
pkgs/development/python-modules/zigpy-znp/default.nix-
pkgs/development/python-modules/zigpy-znp/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/zigpy-znp/default.nix-
pkgs/development/python-modules/zigpy-znp/default.nix-  dependencies = [
pkgs/development/python-modules/zigpy-znp/default.nix-    async-timeout
pkgs/development/python-modules/zigpy-znp/default.nix-    coloredlogs
--
pkgs/development/python-modules/releases/default.nix-  format = "setuptools";
pkgs/development/python-modules/releases/default.nix-
pkgs/development/python-modules/releases/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/releases/default.nix-    owner = "bitprophet";
pkgs/development/python-modules/releases/default.nix-    repo = "releases";
pkgs/development/python-modules/releases/default.nix-    rev = version;
pkgs/development/python-modules/releases/default.nix-    hash = "sha256-IgEKAUk97R3ZvqvexD/ptT8i0uf48K+DKkk4q3pn3G8=";
pkgs/development/python-modules/releases/default.nix-  };
pkgs/development/python-modules/releases/default.nix-
pkgs/development/python-modules/releases/default.nix-  postPatch = ''
pkgs/development/python-modules/releases/default.nix:    substituteInPlace setup.py --replace "semantic_version<2.7" "semantic_version"
pkgs/development/python-modules/releases/default.nix-  '';
pkgs/development/python-modules/releases/default.nix-
pkgs/development/python-modules/releases/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/releases/default.nix-    semantic-version
pkgs/development/python-modules/releases/default.nix-    sphinx
pkgs/development/python-modules/releases/default.nix-  ];
pkgs/development/python-modules/releases/default.nix-
pkgs/development/python-modules/releases/default.nix-  # Test suite doesn't run. See https://github.com/bitprophet/releases/issues/95.
pkgs/development/python-modules/releases/default.nix-  doCheck = false;
pkgs/development/python-modules/releases/default.nix-
--
pkgs/development/python-modules/apache-beam/default.nix-  ];
pkgs/development/python-modules/apache-beam/default.nix-
pkgs/development/python-modules/apache-beam/default.nix-  enableParallelBuilding = true;
pkgs/development/python-modules/apache-beam/default.nix-
pkgs/development/python-modules/apache-beam/default.nix-  postPatch = ''
pkgs/development/python-modules/apache-beam/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/apache-beam/default.nix-      --replace-fail "distlib==0.3.7" "distlib" \
pkgs/development/python-modules/apache-beam/default.nix-      --replace-fail "yapf==0.29.0" "yapf" \
pkgs/development/python-modules/apache-beam/default.nix-      --replace-fail "grpcio-tools==1.62.1" "grpcio-tools" \
pkgs/development/python-modules/apache-beam/default.nix-      --replace-fail "mypy-protobuf==3.5.0" "mypy-protobuf" \
pkgs/development/python-modules/apache-beam/default.nix-      --replace-fail "numpy>=1.14.3,<2.3.0" "numpy"
pkgs/development/python-modules/apache-beam/default.nix-
pkgs/development/python-modules/apache-beam/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/apache-beam/default.nix-      --replace-fail "  copy_tests_from_docs()" ""
pkgs/development/python-modules/apache-beam/default.nix-  '';
pkgs/development/python-modules/apache-beam/default.nix-
pkgs/development/python-modules/apache-beam/default.nix-  __darwinAllowLocalNetworking = true;
pkgs/development/python-modules/apache-beam/default.nix-
pkgs/development/python-modules/apache-beam/default.nix-  pythonImportsCheck = [ "apache_beam" ];
pkgs/development/python-modules/apache-beam/default.nix-
pkgs/development/python-modules/apache-beam/default.nix-  nativeCheckInputs = [
--
pkgs/development/python-modules/python-dateutil/default.nix-  version = "2.9.0.post0";
pkgs/development/python-modules/python-dateutil/default.nix-  pyproject = true;
pkgs/development/python-modules/python-dateutil/default.nix-
pkgs/development/python-modules/python-dateutil/default.nix-  src = fetchPypi {
pkgs/development/python-modules/python-dateutil/default.nix-    inherit pname version;
pkgs/development/python-modules/python-dateutil/default.nix-    hash = "sha256-N91UII2n4c2HU4ghfV4A69QXkkn5D7ckN+kaNUWaCtM=";
pkgs/development/python-modules/python-dateutil/default.nix-  };
pkgs/development/python-modules/python-dateutil/default.nix-
pkgs/development/python-modules/python-dateutil/default.nix-  postPatch = ''
pkgs/development/python-modules/python-dateutil/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/python-dateutil/default.nix-      --replace-fail "setuptools_scm<8.0" "setuptools_scm"
pkgs/development/python-modules/python-dateutil/default.nix-  '';
pkgs/development/python-modules/python-dateutil/default.nix-
pkgs/development/python-modules/python-dateutil/default.nix-  nativeBuildInputs = [ setuptools-scm ];
pkgs/development/python-modules/python-dateutil/default.nix-
pkgs/development/python-modules/python-dateutil/default.nix-  propagatedBuildInputs = [ six ];
pkgs/development/python-modules/python-dateutil/default.nix-
pkgs/development/python-modules/python-dateutil/default.nix-  # cyclic dependency: tests need freezegun, which depends on python-dateutil
pkgs/development/python-modules/python-dateutil/default.nix-  doCheck = false;
pkgs/development/python-modules/python-dateutil/default.nix-
--
--
pkgs/development/python-modules/cocotb/default.nix-
pkgs/development/python-modules/cocotb/default.nix-    # POSIX portability (TODO: upstream this)
pkgs/development/python-modules/cocotb/default.nix-    for f in \
pkgs/development/python-modules/cocotb/default.nix-      cocotb/share/makefiles/Makefile.* \
pkgs/development/python-modules/cocotb/default.nix-      cocotb/share/makefiles/simulators/Makefile.*
pkgs/development/python-modules/cocotb/default.nix-    do
pkgs/development/python-modules/cocotb/default.nix:      substituteInPlace $f --replace 'shell which' 'shell command -v'
pkgs/development/python-modules/cocotb/default.nix-    done
pkgs/development/python-modules/cocotb/default.nix-
pkgs/development/python-modules/cocotb/default.nix-    # remove circular dependency cocotb-bus from setup.py
pkgs/development/python-modules/cocotb/default.nix:    substituteInPlace setup.py --replace "'cocotb-bus<1.0'" ""
pkgs/development/python-modules/cocotb/default.nix-  '';
pkgs/development/python-modules/cocotb/default.nix-
pkgs/development/python-modules/cocotb/default.nix-  disabledTests = [
pkgs/development/python-modules/cocotb/default.nix-    # https://github.com/cocotb/cocotb/commit/425e1edb8e7133f4a891f2f87552aa2748cd8d2c#diff-4df986cbc2b1a3f22172caea94f959d8fcb4a128105979e6e99c68139469960cL33
pkgs/development/python-modules/cocotb/default.nix-    "test_cocotb"
pkgs/development/python-modules/cocotb/default.nix-    "test_cocotb_parallel"
pkgs/development/python-modules/cocotb/default.nix-  ];
pkgs/development/python-modules/cocotb/default.nix-
pkgs/development/python-modules/cocotb/default.nix-  nativeCheckInputs = [
pkgs/development/python-modules/cocotb/default.nix-    cocotb-bus
--
pkgs/development/python-modules/manimpango/default.nix-
pkgs/development/python-modules/manimpango/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/manimpango/default.nix-    owner = "ManimCommunity";
pkgs/development/python-modules/manimpango/default.nix-    repo = "manimpango";
pkgs/development/python-modules/manimpango/default.nix-    tag = "v${version}";
pkgs/development/python-modules/manimpango/default.nix-    hash = "sha256-nN+XOnki8fG7URMy2Fhs2X+yNi8Y7wDo53d61xaRa3w=";
pkgs/development/python-modules/manimpango/default.nix-  };
pkgs/development/python-modules/manimpango/default.nix-
pkgs/development/python-modules/manimpango/default.nix-  postPatch = ''
pkgs/development/python-modules/manimpango/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/manimpango/default.nix-      --replace-fail "Cython>=3.0.2,<3.1" Cython
pkgs/development/python-modules/manimpango/default.nix-  '';
pkgs/development/python-modules/manimpango/default.nix-
pkgs/development/python-modules/manimpango/default.nix-  nativeBuildInputs = [ pkg-config ];
pkgs/development/python-modules/manimpango/default.nix-
pkgs/development/python-modules/manimpango/default.nix-  buildInputs = [ pango ];
pkgs/development/python-modules/manimpango/default.nix-
pkgs/development/python-modules/manimpango/default.nix-  build-system = [
pkgs/development/python-modules/manimpango/default.nix-    setuptools
pkgs/development/python-modules/manimpango/default.nix-    cython
--
--
pkgs/development/python-modules/python-tsp/default.nix-
pkgs/development/python-modules/python-tsp/default.nix-  dependencies = [
pkgs/development/python-modules/python-tsp/default.nix-    numpy
pkgs/development/python-modules/python-tsp/default.nix-    requests
pkgs/development/python-modules/python-tsp/default.nix-    tsplib95
pkgs/development/python-modules/python-tsp/default.nix-  ];
pkgs/development/python-modules/python-tsp/default.nix-
pkgs/development/python-modules/python-tsp/default.nix-  # Rename some dependencies
pkgs/development/python-modules/python-tsp/default.nix-  postPatch = ''
pkgs/development/python-modules/python-tsp/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/python-tsp/default.nix-      --replace-fail "poetry>=0.12" "poetry-core>=0.12" \
pkgs/development/python-modules/python-tsp/default.nix-      --replace-fail "poetry.masonry.api" "poetry.core.masonry.api"
pkgs/development/python-modules/python-tsp/default.nix-  '';
pkgs/development/python-modules/python-tsp/default.nix-
pkgs/development/python-modules/python-tsp/default.nix-  nativeCheckInputs = [
pkgs/development/python-modules/python-tsp/default.nix-    pytestCheckHook
pkgs/development/python-modules/python-tsp/default.nix-    mock
pkgs/development/python-modules/python-tsp/default.nix-  ];
pkgs/development/python-modules/python-tsp/default.nix-
pkgs/development/python-modules/python-tsp/default.nix-  pythonImportsCheck = [ "python_tsp" ];
--
--
pkgs/development/python-modules/vllm/default.nix-    })
pkgs/development/python-modules/vllm/default.nix-    ./0002-setup.py-nix-support-respect-cmakeFlags.patch
pkgs/development/python-modules/vllm/default.nix-    ./0003-propagate-pythonpath.patch
pkgs/development/python-modules/vllm/default.nix-    ./0004-drop-lsmod.patch
pkgs/development/python-modules/vllm/default.nix-    ./0005-drop-intel-reqs.patch
pkgs/development/python-modules/vllm/default.nix-  ];
pkgs/development/python-modules/vllm/default.nix-
pkgs/development/python-modules/vllm/default.nix-  postPatch = ''
pkgs/development/python-modules/vllm/default.nix-    # pythonRelaxDeps does not cover build-system
pkgs/development/python-modules/vllm/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/vllm/default.nix-      --replace-fail "torch ==" "torch >=" \
pkgs/development/python-modules/vllm/default.nix-      --replace-fail "setuptools>=77.0.3,<80.0.0" "setuptools"
pkgs/development/python-modules/vllm/default.nix-
pkgs/development/python-modules/vllm/default.nix-    # Ignore the python version check because it hard-codes minor versions and
pkgs/development/python-modules/vllm/default.nix-    # lags behind `ray`'s python interpreter support
pkgs/development/python-modules/vllm/default.nix:    substituteInPlace CMakeLists.txt \
pkgs/development/python-modules/vllm/default.nix-      --replace-fail \
pkgs/development/python-modules/vllm/default.nix-        'set(PYTHON_SUPPORTED_VERSIONS' \
pkgs/development/python-modules/vllm/default.nix-        'set(PYTHON_SUPPORTED_VERSIONS "${lib.versions.majorMinor python.version}"'
pkgs/development/python-modules/vllm/default.nix-
pkgs/development/python-modules/vllm/default.nix-    # Pass build environment PYTHONPATH to vLLM's Python configuration scripts
pkgs/development/python-modules/vllm/default.nix:    substituteInPlace CMakeLists.txt \
--
pkgs/development/python-modules/pytest-cid/default.nix-
pkgs/development/python-modules/pytest-cid/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/pytest-cid/default.nix-    owner = "ntninja";
pkgs/development/python-modules/pytest-cid/default.nix-    repo = "pytest-cid";
pkgs/development/python-modules/pytest-cid/default.nix-    tag = "v${version}";
pkgs/development/python-modules/pytest-cid/default.nix-    hash = "sha256-dcL/i5+scmdXh7lfE8+32w9PdHWf+mkunJL1vpJ5+Co=";
pkgs/development/python-modules/pytest-cid/default.nix-  };
pkgs/development/python-modules/pytest-cid/default.nix-
pkgs/development/python-modules/pytest-cid/default.nix-  postPatch = ''
pkgs/development/python-modules/pytest-cid/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/pytest-cid/default.nix-      --replace "pytest >= 5.0, < 7.0" "pytest >= 5.0"
pkgs/development/python-modules/pytest-cid/default.nix-  '';
pkgs/development/python-modules/pytest-cid/default.nix-
pkgs/development/python-modules/pytest-cid/default.nix-  nativeBuildInputs = [ flit-core ];
pkgs/development/python-modules/pytest-cid/default.nix-
pkgs/development/python-modules/pytest-cid/default.nix-  propagatedBuildInputs = [ py-cid ];
pkgs/development/python-modules/pytest-cid/default.nix-
pkgs/development/python-modules/pytest-cid/default.nix-  nativeCheckInputs = [
pkgs/development/python-modules/pytest-cid/default.nix-    pytestCheckHook
pkgs/development/python-modules/pytest-cid/default.nix-    pytest-cov-stub
--
--
pkgs/development/python-modules/boilerpy3/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/boilerpy3/default.nix-    owner = "jmriebold";
pkgs/development/python-modules/boilerpy3/default.nix-    repo = "BoilerPy3";
pkgs/development/python-modules/boilerpy3/default.nix-    tag = "v${version}";
pkgs/development/python-modules/boilerpy3/default.nix-    hash = "sha256-dhAB0VbBGsSrgYGUlZEYaKA6sQB/f9Bb3alsRuQ8opo=";
pkgs/development/python-modules/boilerpy3/default.nix-  };
pkgs/development/python-modules/boilerpy3/default.nix-
pkgs/development/python-modules/boilerpy3/default.nix-  postPatch = ''
pkgs/development/python-modules/boilerpy3/default.nix-    # the version mangling in mautrix_signal/get_version.py interacts badly with pythonRelaxDepsHook
pkgs/development/python-modules/boilerpy3/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/boilerpy3/default.nix-      --replace '>=3.6.*' '>=3.6'
pkgs/development/python-modules/boilerpy3/default.nix-  '';
pkgs/development/python-modules/boilerpy3/default.nix-
pkgs/development/python-modules/boilerpy3/default.nix-  pythonImportsCheck = [ "boilerpy3" ];
pkgs/development/python-modules/boilerpy3/default.nix-
pkgs/development/python-modules/boilerpy3/default.nix-  meta = with lib; {
pkgs/development/python-modules/boilerpy3/default.nix-    homepage = "https://github.com/jmriebold/BoilerPy3";
pkgs/development/python-modules/boilerpy3/default.nix-    description = "Python port of Boilerpipe library";
pkgs/development/python-modules/boilerpy3/default.nix-    changelog = "https://github.com/jmriebold/BoilerPy3/releases/tag/v${version}";
pkgs/development/python-modules/boilerpy3/default.nix-    license = licenses.asl20;
--
pkgs/development/python-modules/pytest-harvest/default.nix-    repo = "python-pytest-harvest";
pkgs/development/python-modules/pytest-harvest/default.nix-    tag = version;
pkgs/development/python-modules/pytest-harvest/default.nix-    hash = "sha256-s8QiuUFRTTRhSpLa0DHScKFC9xdu+w2rssWCg8sIjsg=";
pkgs/development/python-modules/pytest-harvest/default.nix-  };
pkgs/development/python-modules/pytest-harvest/default.nix-
pkgs/development/python-modules/pytest-harvest/default.nix-  # create file, that is created by setuptools_scm
pkgs/development/python-modules/pytest-harvest/default.nix-  # we disable this file creation as it touches internet
pkgs/development/python-modules/pytest-harvest/default.nix-  postPatch = ''
pkgs/development/python-modules/pytest-harvest/default.nix-    echo "version = '${version}'" > pytest_harvest/_version.py
pkgs/development/python-modules/pytest-harvest/default.nix-
pkgs/development/python-modules/pytest-harvest/default.nix:    substituteInPlace pytest_harvest/tests/test_lazy_and_harvest.py \
pkgs/development/python-modules/pytest-harvest/default.nix-      --replace-fail "from distutils.version import LooseVersion" "from packaging.version import parse" \
pkgs/development/python-modules/pytest-harvest/default.nix-      --replace-fail "LooseVersion" "parse"
pkgs/development/python-modules/pytest-harvest/default.nix-  '';
pkgs/development/python-modules/pytest-harvest/default.nix-
pkgs/development/python-modules/pytest-harvest/default.nix-  nativeBuildInputs = [
pkgs/development/python-modules/pytest-harvest/default.nix-    setuptools-scm
pkgs/development/python-modules/pytest-harvest/default.nix-  ];
pkgs/development/python-modules/pytest-harvest/default.nix-
--
pkgs/development/python-modules/zope-interface/default.nix-
pkgs/development/python-modules/zope-interface/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/zope-interface/default.nix-    owner = "zopefoundation";
pkgs/development/python-modules/zope-interface/default.nix-    repo = "zope.interface";
pkgs/development/python-modules/zope-interface/default.nix-    tag = version;
pkgs/development/python-modules/zope-interface/default.nix-    hash = "sha256-WrS/YHkEmV1G/Scg0xpyu2uFVWTWnEpajqNDvGioVgc=";
pkgs/development/python-modules/zope-interface/default.nix-  };
pkgs/development/python-modules/zope-interface/default.nix-
pkgs/development/python-modules/zope-interface/default.nix-  postPatch = ''
pkgs/development/python-modules/zope-interface/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/zope-interface/default.nix-      --replace-fail "setuptools < 74" "setuptools"
pkgs/development/python-modules/zope-interface/default.nix-  '';
pkgs/development/python-modules/zope-interface/default.nix-
pkgs/development/python-modules/zope-interface/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/zope-interface/default.nix-
pkgs/development/python-modules/zope-interface/default.nix-  pythonImportsCheck = [ "zope.interface" ];
pkgs/development/python-modules/zope-interface/default.nix-
pkgs/development/python-modules/zope-interface/default.nix-  doCheck = false; # Circular deps.
pkgs/development/python-modules/zope-interface/default.nix-
pkgs/development/python-modules/zope-interface/default.nix-  pythonNamespaces = [ "zope" ];
--
--
pkgs/development/python-modules/qiskit-aer/default.nix-    owner = "Qiskit";
pkgs/development/python-modules/qiskit-aer/default.nix-    repo = "qiskit-aer";
pkgs/development/python-modules/qiskit-aer/default.nix-    tag = version;
pkgs/development/python-modules/qiskit-aer/default.nix-    hash = "sha256-jvapuARJUHgAKFUzGb5MUft01LNefVIXtStJqFnCo90=";
pkgs/development/python-modules/qiskit-aer/default.nix-  };
pkgs/development/python-modules/qiskit-aer/default.nix-
pkgs/development/python-modules/qiskit-aer/default.nix-  postPatch = ''
pkgs/development/python-modules/qiskit-aer/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/qiskit-aer/default.nix-      --replace "'cmake!=3.17,!=3.17.0'," "" \
pkgs/development/python-modules/qiskit-aer/default.nix-      --replace "'pybind11', min_version='2.6'" "'pybind11'" \
pkgs/development/python-modules/qiskit-aer/default.nix-      --replace "pybind11>=2.6" "pybind11" \
pkgs/development/python-modules/qiskit-aer/default.nix-      --replace "scikit-build>=0.11.0" "scikit-build" \
pkgs/development/python-modules/qiskit-aer/default.nix-      --replace "min_version='0.11.0'" ""
pkgs/development/python-modules/qiskit-aer/default.nix-  '';
pkgs/development/python-modules/qiskit-aer/default.nix-
pkgs/development/python-modules/qiskit-aer/default.nix-  nativeBuildInputs = [
pkgs/development/python-modules/qiskit-aer/default.nix-    cmake
pkgs/development/python-modules/qiskit-aer/default.nix-    ninja
--
pkgs/development/python-modules/pystray/default.nix-  patches = [
pkgs/development/python-modules/pystray/default.nix-    # fix test_menu_construct_from_none test case
pkgs/development/python-modules/pystray/default.nix-    # https://github.com/moses-palmer/pystray/pull/133
pkgs/development/python-modules/pystray/default.nix-    (fetchpatch {
pkgs/development/python-modules/pystray/default.nix-      url = "https://github.com/moses-palmer/pystray/commit/813007e3034d950d93a2f3e5b029611c3c9c98ad.patch";
pkgs/development/python-modules/pystray/default.nix-      hash = "sha256-m2LfZcWXSfgxb73dac21VDdMDVz3evzcCz5QjdnfM1U=";
pkgs/development/python-modules/pystray/default.nix-    })
pkgs/development/python-modules/pystray/default.nix-  ];
pkgs/development/python-modules/pystray/default.nix-
pkgs/development/python-modules/pystray/default.nix-  postPatch = ''
pkgs/development/python-modules/pystray/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/pystray/default.nix-      --replace-fail "'sphinx >=1.3.1'" ""
pkgs/development/python-modules/pystray/default.nix-  '';
pkgs/development/python-modules/pystray/default.nix-
pkgs/development/python-modules/pystray/default.nix-  nativeBuildInputs = [
pkgs/development/python-modules/pystray/default.nix-    gobject-introspection
pkgs/development/python-modules/pystray/default.nix-    setuptools
pkgs/development/python-modules/pystray/default.nix-  ];
pkgs/development/python-modules/pystray/default.nix-
pkgs/development/python-modules/pystray/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/pystray/default.nix-    pillow
--
pkgs/development/python-modules/pyxnat/default.nix-
pkgs/development/python-modules/pyxnat/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/pyxnat/default.nix-
pkgs/development/python-modules/pyxnat/default.nix-  propagatedBuildInputs = [
pkgs/development/python-modules/pyxnat/default.nix-    lxml
pkgs/development/python-modules/pyxnat/default.nix-    requests
pkgs/development/python-modules/pyxnat/default.nix-  ];
pkgs/development/python-modules/pyxnat/default.nix-
pkgs/development/python-modules/pyxnat/default.nix-  # pathlib is installed part of python38+ w/o an external package
pkgs/development/python-modules/pyxnat/default.nix-  prePatch = ''
pkgs/development/python-modules/pyxnat/default.nix:    substituteInPlace setup.py --replace-fail "pathlib>=1.0" ""
pkgs/development/python-modules/pyxnat/default.nix-  '';
pkgs/development/python-modules/pyxnat/default.nix-
pkgs/development/python-modules/pyxnat/default.nix-  nativeCheckInputs = [
pkgs/development/python-modules/pyxnat/default.nix-    pytestCheckHook
pkgs/development/python-modules/pyxnat/default.nix-    pytest-cov-stub
pkgs/development/python-modules/pyxnat/default.nix-    matplotlib
pkgs/development/python-modules/pyxnat/default.nix-    networkx
pkgs/development/python-modules/pyxnat/default.nix-    pandas
pkgs/development/python-modules/pyxnat/default.nix-  ];
pkgs/development/python-modules/pyxnat/default.nix-  preCheck = ''
--
pkgs/development/python-modules/spylls/default.nix-  disabled = pythonOlder "3.7";
pkgs/development/python-modules/spylls/default.nix-
pkgs/development/python-modules/spylls/default.nix-  src = fetchPypi {
pkgs/development/python-modules/spylls/default.nix-    inherit pname version;
pkgs/development/python-modules/spylls/default.nix-    hash = "sha256-cEWJLcvTJNNoX2nFp2AGPnj7g5kTckzhgHfPCgyT8iA=";
pkgs/development/python-modules/spylls/default.nix-  };
pkgs/development/python-modules/spylls/default.nix-
pkgs/development/python-modules/spylls/default.nix-  postPatch = ''
pkgs/development/python-modules/spylls/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/spylls/default.nix-    --replace-fail poetry.masonry.api poetry.core.masonry.api \
pkgs/development/python-modules/spylls/default.nix-    --replace-fail "poetry>=" "poetry-core>="
pkgs/development/python-modules/spylls/default.nix-  '';
pkgs/development/python-modules/spylls/default.nix-
pkgs/development/python-modules/spylls/default.nix-  build-system = [ poetry-core ];
pkgs/development/python-modules/spylls/default.nix-
pkgs/development/python-modules/spylls/default.nix-  # no unit tests in source distribution...
pkgs/development/python-modules/spylls/default.nix-  doCheck = false;
pkgs/development/python-modules/spylls/default.nix-
pkgs/development/python-modules/spylls/default.nix-  pythonImportsCheck = [
--
pkgs/development/python-modules/strawberry-graphql/default.nix-  disabled = pythonOlder "3.10";
--
pkgs/development/python-modules/strawberry-graphql/default.nix-  ];
--
pkgs/development/python-modules/crochet/default.nix-
pkgs/development/python-modules/crochet/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/crochet/default.nix-    owner = "itamarst";
pkgs/development/python-modules/crochet/default.nix-    repo = "crochet";
pkgs/development/python-modules/crochet/default.nix-    tag = version;
pkgs/development/python-modules/crochet/default.nix-    hash = "sha256-grymhvCC9zDBKhNnQC0o07hdLPV5KMWb6HSz/ntSbq8=";
pkgs/development/python-modules/crochet/default.nix-  };
pkgs/development/python-modules/crochet/default.nix-
pkgs/development/python-modules/crochet/default.nix-  # fix for python>=3.12
pkgs/development/python-modules/crochet/default.nix-  postPatch = ''
pkgs/development/python-modules/crochet/default.nix:    substituteInPlace versioneer.py \
pkgs/development/python-modules/crochet/default.nix-      --replace-fail "SafeConfigParser()" "ConfigParser()" \
pkgs/development/python-modules/crochet/default.nix-      --replace-fail "parser.readfp" "parser.read_file"
pkgs/development/python-modules/crochet/default.nix-  '';
pkgs/development/python-modules/crochet/default.nix-
pkgs/development/python-modules/crochet/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/crochet/default.nix-
pkgs/development/python-modules/crochet/default.nix-  dependencies = [
pkgs/development/python-modules/crochet/default.nix-    twisted
--
pkgs/development/python-modules/justbackoff/default.nix-    owner = "alexferl";
pkgs/development/python-modules/justbackoff/default.nix-    repo = "justbackoff";
pkgs/development/python-modules/justbackoff/default.nix-    rev = "v${version}";
pkgs/development/python-modules/justbackoff/default.nix-    sha256 = "097j6jxgl4b3z46x9y9z10643vnr9v831vhagrxzrq6nviil2z6l";
pkgs/development/python-modules/justbackoff/default.nix-  };
pkgs/development/python-modules/justbackoff/default.nix-
pkgs/development/python-modules/justbackoff/default.nix-  nativeCheckInputs = [ pytestCheckHook ];
pkgs/development/python-modules/justbackoff/default.nix-
pkgs/development/python-modules/justbackoff/default.nix-  postPatch = ''
pkgs/development/python-modules/justbackoff/default.nix:    substituteInPlace setup.py \
pkgs/development/python-modules/justbackoff/default.nix-      --replace "pytest-runner>=5.2" ""
pkgs/development/python-modules/justbackoff/default.nix-  '';
pkgs/development/python-modules/justbackoff/default.nix-
pkgs/development/python-modules/justbackoff/default.nix-  pythonImportsCheck = [ "justbackoff" ];
pkgs/development/python-modules/justbackoff/default.nix-
pkgs/development/python-modules/justbackoff/default.nix-  meta = with lib; {
pkgs/development/python-modules/justbackoff/default.nix-    description = "Simple backoff algorithm in Python";
pkgs/development/python-modules/justbackoff/default.nix-    homepage = "https://github.com/alexferl/justbackoff";
pkgs/development/python-modules/justbackoff/default.nix-    license = with licenses; [ mit ];
pkgs/development/python-modules/justbackoff/default.nix-    maintainers = with maintainers; [ fab ];
--
--
pkgs/development/python-modules/ipycanvas/default.nix-    inherit pname version;
pkgs/development/python-modules/ipycanvas/default.nix-    hash = "sha256-kh8UgiWLWSm1mTF7XBKZMdgOFr41+jgwCjLnqkz+n4k=";
pkgs/development/python-modules/ipycanvas/default.nix-  };
pkgs/development/python-modules/ipycanvas/default.nix-
pkgs/development/python-modules/ipycanvas/default.nix-  # We relax dependencies here instead of pulling in a patch because upstream
pkgs/development/python-modules/ipycanvas/default.nix-  # has released a new version using hatch-jupyter-builder, but it is not yet
pkgs/development/python-modules/ipycanvas/default.nix-  # trivial to upgrade to that.
pkgs/development/python-modules/ipycanvas/default.nix-  #
pkgs/development/python-modules/ipycanvas/default.nix-  postPatch = ''
pkgs/development/python-modules/ipycanvas/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/ipycanvas/default.nix-      --replace-fail '"jupyterlab>=3,<5",' "" \
pkgs/development/python-modules/ipycanvas/default.nix-  '';
pkgs/development/python-modules/ipycanvas/default.nix-
pkgs/development/python-modules/ipycanvas/default.nix-  build-system = [ hatchling ];
pkgs/development/python-modules/ipycanvas/default.nix-
pkgs/development/python-modules/ipycanvas/default.nix-  env.HATCH_BUILD_NO_HOOKS = true;
pkgs/development/python-modules/ipycanvas/default.nix-
pkgs/development/python-modules/ipycanvas/default.nix-  dependencies = [
pkgs/development/python-modules/ipycanvas/default.nix-    ipywidgets
pkgs/development/python-modules/ipycanvas/default.nix-    numpy
--
--
pkgs/development/python-modules/equinox/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/equinox/default.nix-    owner = "patrick-kidger";
pkgs/development/python-modules/equinox/default.nix-    repo = "equinox";
pkgs/development/python-modules/equinox/default.nix-    tag = "v${version}";
pkgs/development/python-modules/equinox/default.nix-    hash = "sha256-zXgAuFGWKHShKodi9swnWIry4VU9s4pBhBRoK5KzaL0=";
pkgs/development/python-modules/equinox/default.nix-  };
pkgs/development/python-modules/equinox/default.nix-
pkgs/development/python-modules/equinox/default.nix-  # Relax speed constraints on tests that can fail on busy builders
pkgs/development/python-modules/equinox/default.nix-  postPatch = ''
pkgs/development/python-modules/equinox/default.nix:    substituteInPlace tests/test_while_loop.py \
pkgs/development/python-modules/equinox/default.nix-      --replace-fail "speed < 0.1" "speed < 0.5" \
pkgs/development/python-modules/equinox/default.nix-      --replace-fail "speed < 0.5" "speed < 1" \
pkgs/development/python-modules/equinox/default.nix-      --replace-fail "speed < 1" "speed < 4" \
pkgs/development/python-modules/equinox/default.nix-  '';
pkgs/development/python-modules/equinox/default.nix-
pkgs/development/python-modules/equinox/default.nix-  build-system = [ hatchling ];
pkgs/development/python-modules/equinox/default.nix-
pkgs/development/python-modules/equinox/default.nix-  dependencies = [
pkgs/development/python-modules/equinox/default.nix-    jax
pkgs/development/python-modules/equinox/default.nix-    jaxtyping
--
pkgs/development/python-modules/dask-glm/default.nix-
pkgs/development/python-modules/dask-glm/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/dask-glm/default.nix-    owner = "dask";
pkgs/development/python-modules/dask-glm/default.nix-    repo = "dask-glm";
pkgs/development/python-modules/dask-glm/default.nix-    tag = version;
pkgs/development/python-modules/dask-glm/default.nix-    hash = "sha256-q98QMmw1toashimS16of54cgZgIPqkua3xGD1FZ1nTc=";
pkgs/development/python-modules/dask-glm/default.nix-  };
pkgs/development/python-modules/dask-glm/default.nix-
pkgs/development/python-modules/dask-glm/default.nix-  # ValueError: The truth value of an empty array is ambiguous. Use `array.size > 0` to check that an array is not empty.
pkgs/development/python-modules/dask-glm/default.nix-  postPatch = ''
pkgs/development/python-modules/dask-glm/default.nix:    substituteInPlace dask_glm/utils.py \
pkgs/development/python-modules/dask-glm/default.nix-      --replace-fail "if arr:" "if (arr is not None) and (arr.size > 0):"
pkgs/development/python-modules/dask-glm/default.nix-  '';
pkgs/development/python-modules/dask-glm/default.nix-
pkgs/development/python-modules/dask-glm/default.nix-  build-system = [ setuptools-scm ];
pkgs/development/python-modules/dask-glm/default.nix-
pkgs/development/python-modules/dask-glm/default.nix-  dependencies = [
pkgs/development/python-modules/dask-glm/default.nix-    cloudpickle
pkgs/development/python-modules/dask-glm/default.nix-    distributed
pkgs/development/python-modules/dask-glm/default.nix-    multipledispatch
pkgs/development/python-modules/dask-glm/default.nix-    scikit-learn
--
--
pkgs/development/python-modules/transaction/default.nix-
pkgs/development/python-modules/transaction/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/transaction/default.nix-    owner = "zopefoundation";
pkgs/development/python-modules/transaction/default.nix-    repo = "transaction";
pkgs/development/python-modules/transaction/default.nix-    tag = version;
pkgs/development/python-modules/transaction/default.nix-    hash = "sha256-8yvA2dvB69+EqsAa+hc93rgg6D64lcajl6JgFabhjwY=";
pkgs/development/python-modules/transaction/default.nix-  };
pkgs/development/python-modules/transaction/default.nix-
pkgs/development/python-modules/transaction/default.nix-  postPatch = ''
pkgs/development/python-modules/transaction/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/transaction/default.nix-      --replace-fail "setuptools<74" "setuptools"
pkgs/development/python-modules/transaction/default.nix-  '';
pkgs/development/python-modules/transaction/default.nix-
pkgs/development/python-modules/transaction/default.nix-  build-system = [
pkgs/development/python-modules/transaction/default.nix-    setuptools
pkgs/development/python-modules/transaction/default.nix-  ];
pkgs/development/python-modules/transaction/default.nix-
pkgs/development/python-modules/transaction/default.nix-  dependencies = [
pkgs/development/python-modules/transaction/default.nix-    zope-interface
pkgs/development/python-modules/transaction/default.nix-  ];
--
--
pkgs/development/python-modules/zope-filerepresentation/default.nix-
pkgs/development/python-modules/zope-filerepresentation/default.nix-  src = fetchFromGitHub {
pkgs/development/python-modules/zope-filerepresentation/default.nix-    owner = "zopefoundation";
pkgs/development/python-modules/zope-filerepresentation/default.nix-    repo = "zope.filerepresentation";
pkgs/development/python-modules/zope-filerepresentation/default.nix-    tag = version;
pkgs/development/python-modules/zope-filerepresentation/default.nix-    hash = "sha256-6J4munk2yyZ6e9rpU2Op+Gbf0OXGI6GpHjmpUZVRjsY=";
pkgs/development/python-modules/zope-filerepresentation/default.nix-  };
pkgs/development/python-modules/zope-filerepresentation/default.nix-
pkgs/development/python-modules/zope-filerepresentation/default.nix-  postPatch = ''
pkgs/development/python-modules/zope-filerepresentation/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/zope-filerepresentation/default.nix-      --replace-fail "setuptools <= 75.6.0" setuptools
pkgs/development/python-modules/zope-filerepresentation/default.nix-  '';
pkgs/development/python-modules/zope-filerepresentation/default.nix-
pkgs/development/python-modules/zope-filerepresentation/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/zope-filerepresentation/default.nix-
pkgs/development/python-modules/zope-filerepresentation/default.nix-  dependencies = [
pkgs/development/python-modules/zope-filerepresentation/default.nix-    zope-interface
pkgs/development/python-modules/zope-filerepresentation/default.nix-    zope-schema
pkgs/development/python-modules/zope-filerepresentation/default.nix-  ];
pkgs/development/python-modules/zope-filerepresentation/default.nix-
--
--
pkgs/development/python-modules/zodbpickle/default.nix-
pkgs/development/python-modules/zodbpickle/default.nix-  disabled = pythonOlder "3.8";
pkgs/development/python-modules/zodbpickle/default.nix-
pkgs/development/python-modules/zodbpickle/default.nix-  src = fetchPypi {
pkgs/development/python-modules/zodbpickle/default.nix-    inherit pname version;
pkgs/development/python-modules/zodbpickle/default.nix-    hash = "sha256-WoUUT7psNPxnvQDH8InW1TLcQ6A0R9/F4jhGyRkjCkU=";
pkgs/development/python-modules/zodbpickle/default.nix-  };
pkgs/development/python-modules/zodbpickle/default.nix-
pkgs/development/python-modules/zodbpickle/default.nix-  postPatch = ''
pkgs/development/python-modules/zodbpickle/default.nix:    substituteInPlace pyproject.toml \
pkgs/development/python-modules/zodbpickle/default.nix-      --replace-fail "setuptools <= 75.6.0" "setuptools"
pkgs/development/python-modules/zodbpickle/default.nix-  '';
pkgs/development/python-modules/zodbpickle/default.nix-
pkgs/development/python-modules/zodbpickle/default.nix-  build-system = [ setuptools ];
pkgs/development/python-modules/zodbpickle/default.nix-
pkgs/development/python-modules/zodbpickle/default.nix-  pythonImportsCheck = [ "zodbpickle" ];
pkgs/development/python-modules/zodbpickle/default.nix-
pkgs/development/python-modules/zodbpickle/default.nix-  nativeCheckInputs = [ pytestCheckHook ];
pkgs/development/python-modules/zodbpickle/default.nix-
pkgs/development/python-modules/zodbpickle/default.nix-  preCheck = ''
--
```
