{
  'targets': [
    {
      'target_name': 'cuda-napi-native',
      'sources': [ 'src/cuda_napi.cc' ],
      'variables': {
        'cuda_root%': '<!(echo %CUDA_PATH%)',
        'cuda_samples%': '<!(echo %NVCUDASAMPLES_ROOT%)',
      },
      'libraries': [
        '-l<(cuda_root)/lib/x64/nvrtc.lib',
        '-l<(cuda_root)/lib/x64/cuda.lib',
        '-l<(cuda_root)/lib/x64/cudart.lib'
      ],
      'include_dirs': [
        "src/includes",
        "<!@(node -p \"require('node-addon-api').include\")",
        "<(cuda_root)/include",
        "<(cuda_samples)/common/inc"
      ],
      'dependencies': [
        "<!(node -p \"require('node-addon-api').gyp\")"
      ],
      '_cflags': ['/std:c++latest'],
      'cflags!': [ '-fno-exceptions' ],
      'cflags_cc!': [ '-fno-exceptions' ],
      'xcode_settings': {
        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
        'CLANG_CXX_LIBRARY': 'libc++',
        'MACOSX_DEPLOYMENT_TARGET': '10.7'
      },
      'msvs_settings': {
        'VCCLCompilerTool': { 'ExceptionHandling': 1 },
      }
    }
  ]
}