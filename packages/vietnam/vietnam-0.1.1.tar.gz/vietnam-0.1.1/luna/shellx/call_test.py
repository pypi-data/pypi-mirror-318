from .call import Call


def test_run_basic_cmd():
    call = Call(["echo", "hello"])
    call()
    call.wait()
    assert call.out == b"hello\n"
    assert call.err == b""
    assert call.returncode == 0


def test_chain_output():
    c1 = Call(["echo", "-n", "hello"])
    c1()
    c2 = Call(["wc", "-c"])
    c2(c1.out)
    assert c2.out.strip() == b"5"


def test_chain_stdout():
    c1 = Call(["echo", "-n", "hello"])
    c1()
    c2 = Call(["wc", "-c"])
    c2(c1.stdout)
    assert c2.out.strip() == b"5"


def test_run_with_cwd():
    call = Call(["pwd"], cwd="/")
    call()
    call.wait()
    assert call.out == b"/\n"
    assert call.err == b""
    assert call.returncode == 0


def test_run_with_env():
    call = Call(["env"], env={"PATH": "/usr/bin"})
    call()
    call.wait()
    assert call.out.strip() == b"PATH=/usr/bin"
    assert call.err == b""
    assert call.returncode == 0
