import os
import shutil

import allure_combine

from huskypo import logstack
from trying.common import Path


def output_allure_html():
    """
    整合 allure result ，並匯出獨立的 html 報告
    """
    os.makedirs(Path.REPORTS_DIR, exist_ok=True)

    tmp_dir = os.path.join(Path.REPORTS_DIR, 'allure_tmp')  # pytest.ini
    index_dir = os.path.join(Path.REPORTS_DIR, 'allure_index')
    os.makedirs(index_dir, exist_ok=True)

    # generate tmp to report dir which contains index.html
    try:
        os.system(f'allure generate {tmp_dir} --clean -o {index_dir}')
        logstack.info(f'✅ 成功: 已整合 tmp_dir 為新的 index_dir: {index_dir}')
    except Exception as e:
        logstack.error(f'❌ 失敗: 未整合 tmp_dir 為新的 index_dir: {index_dir}\n{e}')

    # combine all dir with index.html and generate complete.html
    try:
        allure_combine.combine_allure(index_dir)
        logstack.info(f'✅ 成功: 已生成 complete.html 於 index_dir: {index_dir}')
    except Exception as e:
        logstack.error(f'❌ 失敗: 未生成 complete.html 於 index_dir: {index_dir}\n{e}')
        logstack.warning(f'🟡 請確認 allure commandline 版本介於 2.21.0 和 2.22.0 之間')

    # default expand screenshot of complete.html
    try:
        report_src = f"{index_dir}/complete.html"
        report_dst = f"{Path.REPORTS_DIR}/complete.html"
        os.rename(report_src, report_dst)
        logstack.info(f'✅ 成功: 已移動 complete.html 到資料夾: {Path.REPORTS_DIR}')
    except Exception as e:
        logstack.error('❌ 失敗: 請確認 最終report路徑 及 展開截圖的設定 是否有誤')

    # remove allure result and report directory and files
    try:
        shutil.rmtree(tmp_dir, ignore_errors=True)
        shutil.rmtree(index_dir, ignore_errors=True)
        logstack.info(f'✅ 成功: 已移除 index_dir: {index_dir}')
        logstack.info(f'✅ 成功: 已移除 tmp_dir  :   {tmp_dir}')
    except Exception as e:
        logstack.error(f'❌ 失敗: 移除 tmp_dir 和 index_dir 時發生錯誤，請確認路徑是否正確')
