from pgbackup import storage
import tempfile
import pytest

@pytest.fixture
def infile():
    f = tempfile.TemporaryFile()
    f.write(b'testing')
    f.seek(0)
    return f

def test_storing_file_locally(infile):
    """
    writes content from one file-like to another
    """
    outfile = tempfile.NamedTemporaryFile(delete=False)
    storage.local(infile, outfile)
    with open(outfile.name, 'rb') as f:
        assert f.read() == b'testing'

def test_storing_file_on_s3(mocker, infile):
    """
    writes content from one file-like to S3
    """
    client = mocker.Mock()

    storage.s3(client, infile, 'bucket','file-name')
    client.upload_fileobj.assert_called_with(infile,"bucket","file-name")

