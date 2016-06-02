from pytestskeleton.skeleton import Generator


def test_skeleton_generator_get_file_list():
    result = Generator.list_files('/tmp/')
    assert result
