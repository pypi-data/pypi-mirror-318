""" testen voor de package waterstand """
import unittest
from unittest.mock import patch, MagicMock, ANY
from urllib.error import HTTPError, URLError

import waterstand


class TestUrlopen(unittest.TestCase):

  @patch('urllib.request.urlopen')
  def test_haalwaterstand(self, mock_urlopen):
    f = open('tests/testdata.json', 'r')
    testdata = f.read()

    mock_response = MagicMock()
    mock_response.getcode.return_value = 200
    mock_response.read.return_value = testdata.encode('utf-8')
    mock_response.__enter__.return_value = mock_response

    mock_urlopen.return_value = mock_response

    response = waterstand.haalwaterstand('Katerveer', 'KATV')

    self.assertEqual(response, {'resultaat': 'OK', 'tijd': '23-11 16:50', 'nu': 84.0, 'morgen': 89.0})

  @patch('urllib.request.urlopen')
  def test_haalwaterstand_timeformat(self, mock_urlopen):
    f = open('tests/testdata2.json', 'r')
    testdata = f.read()

    mock_response = MagicMock()
    mock_response.getcode.return_value = 200
    mock_response.read.return_value = testdata.encode('utf-8')
    mock_response.__enter__.return_value = mock_response

    mock_urlopen.return_value = mock_response

    response = waterstand.haalwaterstand('Katerveer', 'KATV')

    self.assertEqual(response, {'resultaat': 'OK', 'tijd': '23-11 16:50', 'nu': 84.0, 'morgen': 89.0})

  @patch('urllib.request.urlopen', side_effect=HTTPError(None, None, None, None, None))
  def test_haalwaterstand_httperror(self, mock_urlopen):
    response = waterstand.haalwaterstand('Katerveer', 'KATV')

    expected = {'resultaat': 'NOK', 'error': ANY}
    self.assertEqual(response, expected)

  @patch('urllib.request.urlopen', side_effect=TimeoutError)
  def test_haalwaterstand_timeouterror(self, mock_urlopen):
    response = waterstand.haalwaterstand('Katerveer', 'KATV')

    expected = {'resultaat': 'NOK', 'error': ANY}
    self.assertEqual(response, expected)

  @patch('urllib.request.urlopen', side_effect=URLError('Dummy'))
  def test_haalwaterstand_urlerror(self, mock_urlopen):
    response = waterstand.haalwaterstand('Katerveer', 'KATV')

    expected = {'resultaat': 'NOK', 'error': ANY}
    self.assertEqual(response, expected)
