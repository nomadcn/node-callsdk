{
    'targets': [
        {
            'target_name': '<(module_name)',
            'sources': [
                './src/addon.cc',
                './src/ext/gwutils/Flags.cpp',
                './src/ext/gwutils/Logger.cpp',
                './src/ext/gwutils/ThreadSafe.cpp'
            ],

            'include_dirs': [
                './src/ext/gwutils',
                './src/ext/nablesdk/win32/include'
            ],

            'conditions': [
                ['OS == "win"', {
                    'libraries': [
                        '../src/ext/nablesdk/win32/lib/release/ScfAgentSDK.lib'
                    ],
                    'configurations' : {
                        'Debug' : {
                            'msvs_settings': {
                                'VCCLCompilerTool': {
                                    'RuntimeLibrary': '3' # /MDd
                                },
                                'VCLinkerTool': {
                                    'AdditionalOptions': ['/ignore:4099'],
                                    'IgnoreDefaultLibraryNames': ['libcmtd.lib']
                                }
                            }
                        },
                        'Release' : {
                            'msvs_settings': {
                                'VCCLCompilerTool': {
                                    'RuntimeTypeInfo': 'true', # To disable '/GR-'
                                    'RuntimeLibrary': '2' # /MDd
                                },
                                'VCLinkerTool': {
                                    'AdditionalOptions': ['/ignore:4099'],
                                    'IgnoreDefaultLibraryNames': ['libcmt.lib']
                                }
                            }
                        }
                    }
                }],
                ['OS == "mac"', {
                    'xcode_settings': {
                        'GCC_ENABLE_CPP_RTTI': 'YES',
                        "OTHER_CFLAGS": [
                            "-D__MAC_OS__ -DOSX"
                        ]
                    },
                    'libraries': [
                        '../src/ext/nablesdk/mac/lib/release/libScfAgentSDK.a'
                    ]
                }]
            ]
        },
        {
            "target_name": "action_after_build",
            "type": "none",
            "dependencies": [ "<(module_name)" ],
            "copies": [
                {
                    "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
                    "destination": "<(module_path)"
                }
            ]
        }
    ]
}
