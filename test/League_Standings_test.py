import os
import pytest

from app.League_Standings import findStandings

CI_ENV = os.getenv("CI") == "true"

@pytest.mark.skipif(CI_ENV==True, reason="to avoid issuing HTTP requests on the CI server")

def test_findStandings():
    
