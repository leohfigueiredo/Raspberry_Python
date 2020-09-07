import pytest

#@pytest.fixture(scope="module")
@pytest.fixture(scope="session")
#@pytest.fixture(scope="function")
#@pytest.fixture(scope="class")
def fixture01(request):
	print("\nIn fixture...")
	print("Fixture Scope: " + str(request.scope))
	print("Function Name: " + str(request.function.__name__))
	print("Class Name: " + str(request.cls))
	print("Module Name: " + str(request.module.__name__))
	print("File Path: " + str(request.fspath))

@pytest.mark.usefixtures('fixture01')
def test_case01():
	print("\nI am the test case...")
