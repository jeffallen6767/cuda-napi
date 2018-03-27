const addon = require('../build/Release/cuda-napi-native');

function CudaNapi(options) {
  
    this.info = function() {
        return _addonInstance.info();
    }

    var _addonInstance = new addon.CudaNapi(options);
}

module.exports = CudaNapi;
