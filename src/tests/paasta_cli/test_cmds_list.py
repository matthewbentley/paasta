from mock import patch, MagicMock
from StringIO import StringIO

from service_deployment_tools.paasta_cli.cmds.list import paasta_list


@patch('service_deployment_tools.paasta_cli.cmds.list.read_services_configuration')
@patch('sys.stdout', new_callable=StringIO)
def test_list_paasta_list(mock_stdout, mock_read_services):
    # paasta_list print each service returned by get_services

    attrs = {'keys.return_value': ['service_1', 'service_2']}

    mock_function = MagicMock()
    mock_function.configure_mock(**attrs)
    mock_read_services.return_value = mock_function

    args = ['./paasta_cli', 'list']
    paasta_list(args)
    output = mock_stdout.getvalue()
    assert output == 'service_1\nservice_2\n'