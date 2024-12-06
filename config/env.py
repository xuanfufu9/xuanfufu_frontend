import argparse
import os
from dotenv import load_dotenv
from functools import lru_cache
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    """
    应用配置
    """

    app_env: str = 'dev'
    app_name: str = 'DF Admin'
    app_base_url: str = 'http://127.0.0.1:9099'
    app_proxy_path: str = '/dev-api'
    app_is_proxy: bool = False
    app_secret_key: str = 'Dash-FastAPI-Admin'
    app_host: str = '0.0.0.0'
    app_port: int = 8088
    app_debug: bool = True
    app_compress_algorithm: str = 'br'
    app_compress_br_level: int = 11


class CacheSettings(BaseSettings):
    """
    缓存配置
    """

    lru_cache_maxsize: int = 10000
    lru_cache_capacity: int = 10000
    ttl_cache_maxsize: int = 0
    ttl_cache_expire: int = 600


class GetConfig:
    """
    获取配置
    """

    def __init__(self):
        self.parse_cli_args()

    @lru_cache()
    def get_app_config(self):
        """
        获取应用配置
        """
        # 实例化应用配置模型
        return AppSettings()

    @lru_cache()
    def get_cache_config(self):
        """
        获取缓存配置
        """
        # 实例化缓存配置模型
        return CacheSettings()

    @staticmethod
    def parse_cli_args():
        """
        解析命令行参数
        """
        # 使用argparse定义命令行参数
        parser = argparse.ArgumentParser(description='命令行参数')
        parser.add_argument('--env', type=str, default='', help='运行环境')
        # 解析命令行参数
        args = parser.parse_args()
        # 设置环境变量，如果未设置命令行参数，默认APP_ENV为dev
        os.environ['APP_ENV'] = args.env if args.env else 'dev'
        # 读取运行环境
        run_env = os.environ.get('APP_ENV', '')
        # 运行环境未指定时默认加载.env.dev
        env_file = '.env.dev'
        # 运行环境不为空时按命令行参数加载对应.env文件
        if run_env != '':
            env_file = f'.env.{run_env}'
        # 加载配置
        load_dotenv(env_file)


# 实例化获取配置类
get_config = GetConfig()
# 应用配置
AppConfig = get_config.get_app_config()
# 缓存配置
CacheConfig = get_config.get_cache_config()


class ApiConfig:
    """
    Api配置

    BaseUrl: Api请求地址
    """

    BaseUrl = (
        AppConfig.app_base_url + AppConfig.app_proxy_path
        if AppConfig.app_is_proxy
        else AppConfig.app_base_url
    )


class PathConfig:
    """
    路径配置

    ABS_ROOT_PATH: 项目绝对根目录
    """

    ABS_ROOT_PATH = os.path.abspath(os.getcwd())


class IconConfig:
    ICON_LIST = [
        'antd-carry-out',
        'antd-car',
        'antd-bulb',
        'antd-build',
        'antd-bug',
        'antd-bar-code',
        'antd-branches',
        'antd-aim',
        'antd-issues-close',
        'antd-ellipsis',
        'antd-user',
        'antd-unlock',
        'antd-repair',
        'antd-team',
        'antd-sync',
        'antd-setting',
        'antd-send',
        'antd-schedule',
        'antd-save',
        'antd-rocket',
        'antd-reload',
        'antd-read',
        'antd-qrcode',
        'antd-power-off',
        'antd-number',
        'antd-notification',
        'antd-menu',
        'antd-mail',
        'antd-lock',
        'antd-loading',
        'antd-key',
        'antd-hourglass',
        'antd-global',
        'antd-function',
        'antd-import',
        'antd-export',
        'antd-dashboard',
        'antd-control',
        'antd-console-sql',
        'antd-compass',
        'antd-comment',
        'antd-code',
        'antd-cluster',
        'antd-clear',
        'antd-camera',
        'antd-book',
        'antd-catalog',
        'antd-api',
        'antd-alert',
        'antd-account-book',
        'antd-alipay',
        'antd-alipay-circle',
        'antd-weibo',
        'antd-github',
        'antd-fall',
        'antd-rise',
        'antd-stock',
        'antd-home',
        'antd-fund',
        'antd-area-chart',
        'antd-radar-chart',
        'antd-bar-chart',
        'antd-pie-chart',
        'antd-box-plot',
        'antd-dot-chart',
        'antd-line-chart',
        'antd-field-binary',
        'antd-field-number',
        'antd-field-string',
        'antd-field-time',
        'antd-file-add',
        'antd-file-done',
        'antd-file',
        'antd-file-image',
        'antd-file-markdown',
        'antd-file-pdf',
        'antd-file-protect',
        'antd-file-sync',
        'antd-file-text',
        'antd-file-word',
        'antd-file-zip',
        'antd-filter',
        'antd-fire',
        'antd-woman',
        'antd-arrow-up',
        'antd-arrow-down',
        'antd-arrow-left',
        'antd-arrow-right',
        'antd-flag',
        'antd-user-add',
        'antd-folder-add',
        'antd-man',
        'antd-tag',
        'antd-folder',
        'antd-user-delete',
        'antd-trophy',
        'antd-shopping-cart',
        'antd-folder-open',
        'antd-fork',
        'antd-select',
        'antd-tags',
        'antd-thunderbolt',
        'antd-sound',
        'antd-fund-projection-screen',
        'antd-funnel-plot',
        'antd-gift',
        'antd-robot',
        'antd-pushpin',
        'antd-printer',
        'antd-phone',
        'antd-picture',
        'antd-idcard',
        'antd-partition',
        'antd-monitor',
        'antd-more',
        'antd-apartment',
        'antd-money-collect',
        'antd-experiment',
        'antd-link',
        'antd-mobile',
        'antd-coffee',
        'antd-layout',
        'antd-eye',
        'antd-eye-invisible',
        'antd-exception',
        'antd-dollar',
        'antd-euro',
        'antd-download',
        'antd-environment',
        'antd-deployment-unit',
        'antd-crown',
        'antd-desktop',
        'antd-like',
        'antd-dislike',
        'antd-disconnect',
        'antd-app-store',
        'antd-app-store-add',
        'antd-bell',
        'antd-calculator',
        'antd-calendar',
        'antd-database',
        'antd-history',
        'antd-search',
        'antd-file-search',
        'antd-cloud',
        'antd-cloud-upload',
        'antd-cloud-download',
        'antd-cloud-server',
        'antd-cloud-sync',
        'antd-swap',
        'antd-rollback',
        'antd-login',
        'antd-logout',
        'antd-menu-fold',
        'antd-menu-unfold',
        'antd-full-screen',
        'antd-full-screen-exit',
        'antd-question-circle',
        'antd-plus-circle',
        'antd-minus-circle',
        'antd-info-circle',
        'antd-exclamation-circle',
        'antd-close-circle',
        'antd-check-circle',
        'antd-clock-circle',
        'antd-stop',
        'antd-edit',
        'antd-delete',
        'antd-highlight',
        'antd-redo',
        'antd-undo',
        'antd-zoom-in',
        'antd-zoom-out',
        'antd-sort-ascending',
        'antd-sort-descending',
        'antd-table',
        'antd-question',
        'antd-plus',
        'antd-minus',
        'antd-close',
        'antd-check',
        'antd-sketch',
        'antd-bank',
        'antd-block',
        'antd-insurance',
        'antd-smile',
        'antd-skin',
        'antd-star',
        'antd-right-circle-two-tone',
        'antd-left-circle-two-tone',
        'antd-up-circle-two-tone',
        'antd-down-circle-two-tone',
        'antd-up-square-two-tone',
        'antd-down-square-two-tone',
        'antd-left-square-two-tone',
        'antd-right-square-two-tone',
        'antd-question-circle-two-tone',
        'antd-plus-circle-two-tone',
        'antd-minus-circle-two-tone',
        'antd-plus-square-two-tone',
        'antd-minus-square-two-tone',
        'antd-info-circle-two-tone',
        'antd-exclamation-circle-two-tone',
        'antd-close-circle-two-tone',
        'antd-close-square-two-tone',
        'antd-check-circle-two-tone',
        'antd-check-square-two-tone',
        'antd-edit-two-tone',
        'antd-delete-two-tone',
        'antd-highlight-two-tone',
        'antd-pie-chart-two-tone',
        'antd-box-chart-two-tone',
        'antd-fund-two-tone',
        'antd-sliders-two-tone',
        'antd-api-two-tone',
        'antd-cloud-two-tone',
        'antd-hourglass-two-tone',
        'antd-notification-two-tone',
        'antd-tool-two-tone',
        'antd-down',
        'antd-up',
        'antd-left',
        'antd-right',
        'md-star-half',
        'md-star-border',
        'md-star',
        'md-people',
        'md-plus-one',
        'md-notifications',
        'md-pin-drop',
        'md-layers-clear',
        'md-layers',
        'md-edit-location',
        'md-tune',
        'md-transform',
        'md-timer-off',
        'md-timer',
        'md-file-upload',
        'md-file-download',
        'md-create-new-folder',
        'md-cloud-upload',
        'md-cloud-queue',
        'md-cloud-download',
        'md-cloud-done',
        'md-insert-chart',
        'md-functions',
        'md-format-quote',
        'md-attach-file',
        'md-storage',
        'md-save',
        'md-remove-circle-outline',
        'md-remove-circle',
        'md-remove',
        'md-low-priority',
        'md-link',
        'md-gesture',
        'md-forward',
        'md-flag',
        'md-drafts',
        'md-create',
        'md-content-paste',
        'md-content-cut',
        'md-content-copy',
        'md-clear',
        'md-block',
        'md-backspace',
        'md-add-box',
        'md-add',
        'md-add-circle-outline',
        'md-add-circle',
        'md-location-on',
        'md-mail-outline',
        'md-email',
        'md-not-interested',
        'md-library-books',
        'md-library-add',
        'md-equalizer',
        'md-add-alert',
        'md-visibility-off',
        'md-visibility',
        'md-verified-user',
        'md-update',
        'md-trending-up',
        'md-trending-flat',
        'md-trending-down',
        'md-translate',
        'md-toc',
        'md-timeline',
        'md-thumb-up',
        'md-thumb-down',
        'md-swap-vert',
        'md-swap-horiz',
        'md-supervisor-account',
        'md-subject',
        'md-settings',
        'md-search',
        'md-schedule',
        'md-restore',
        'md-query-builder',
        'md-power-settings-new',
        'md-opacity',
        'md-note-add',
        'md-lock-outline',
        'md-lock-open',
        'md-list',
        'md-lightbulb-outline',
        'md-launch',
        'md-label-outline',
        'md-label',
        'md-input',
        'md-info-outline',
        'md-info',
        'md-hourglass',
        'md-home',
        'md-history',
        'md-highlight-off',
        'md-help-outline',
        'md-help',
        'md-get-app',
        'md-translate',
        'md-fingerprint',
        'md-findIn-page',
        'md-favorite-border',
        'md-favorite',
        'md-extension',
        'md-explore',
        'md-exit-to-app',
        'md-event',
        'md-description',
        'md-delete-forever',
        'md-delete',
        'md-dashboard',
        'md-code',
        'md-build',
        'md-bug-report',
        'md-assignment',
        'md-assessment',
        'md-alarm-on',
        'md-alarm-off',
        'md-alarm-add',
        'md-alarm',
        'md-account-circle',
        'fc-vlc',
        'fc-view-details',
        'fc-upload',
        'fc-tree-structure',
        'fc-timeline',
        'fc-template',
        'fc-survey',
        'fc-signature',
        'fc-share',
        'fc-services',
        'fc-rules',
        'fc-questions',
        'fc-process',
        'fc-plus',
        'fc-overtime',
        'fc-organization',
        'fc-numerical-sorting21',
        'fc-numerical-sorting12',
        'fc-multiple-inputs',
        'fc-mind-map',
        'fc-menu',
        'fc-list',
        'fc-like',
        'fc-like-placeholder',
        'fc-info',
        'fc-import',
        'fc-image-file',
        'fc-idea',
        'fc-home',
        'fc-high-priority',
        'fc-low-priority',
        'fc-genealogy',
        'fc-full-trash',
        'fc-document-search',
        'fc-file',
        'fc-faq',
        'fc-export',
        'fc-empty-trash',
        'fc-download',
        'fc-document',
        'fc-deployment',
        'fc-delete-database',
        'fc-conference-call',
        'fc-database',
        'fc-data-protection',
        'fc-data-encryption',
        'fc-data-configuration',
        'fc-data-backup',
        'fc-checkmark',
        'fc-cancel',
        'fc-briefcase',
        'fc-binoculars',
        'fc-automatic',
        'fc-alphabetical-sorting-za',
        'fc-alphabetical-sorting-az',
        'fc-add-database',
        'fc-accept-database',
        'fc-about',
        'fc-radar-chart',
        'fc-scatter-chart',
        'fc-pie-chart',
        'fc-line-chart',
        'fc-flow-chart',
        'fc-doughnut-chart',
        'fc-bar-chart',
        'fc-area-chart',
        'fc-line-bar-chart',
        'fc-workflow',
        'fc-todo-list',
        'fc-synchronize',
        'fc-repair',
        'fc-statistics',
        'fc-settings',
        'fc-search',
        'fc-serial-tasks',
        'fc-safe',
        'fc-negative-dynamic',
        'fc-positive-dynamic',
        'fc-planner',
        'fc-parallel-tasks',
        'fc-org-unit',
        'fc-opened-folder',
        'fc-ok',
        'fc-inspection',
        'fc-globe',
        'fc-folder',
        'fc-electronics',
        'fc-data-sheet',
        'fc-command-line',
        'fc-calendar',
        'fc-calculator',
        'fc-bullish',
        'fc-bearish',
        'fc-bookmark',
        'fc-approval',
        'fc-advertising',
        'di-linux',
        'di-python',
        'di-chrome',
        'di-database',
        'di-firefox',
        'di-markdown',
        'di-postgresql',
        'di-terminal',
        'di-windows',
        'bi-table',
        'bi-analyse',
        'bi-layer',
        'bi-layer-minus',
        'bi-layer-plus',
        'bs-list-task',
        'bs-list-check',
        'bs-link',
        'bs-link-45-deg',
        'bs-envelope-open',
        'bs-envelope',
        'bs-alarm',
        'gi-mesh-network',
        'im-earth',
        'im-sphere',
    ]
