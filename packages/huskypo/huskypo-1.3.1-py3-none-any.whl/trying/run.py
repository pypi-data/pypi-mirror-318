
import os
import sys
repo_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(repo_path)


if __name__ == '__main__':

    from huskypo import logconfig
    import pytest
    # from trying import allure_generator

    logconfig.basic()
    pytest.main()
    # allure_generator.output_allure_html()
