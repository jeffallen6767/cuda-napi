#pragma once

#include <napi.h>

#include <nlohmann/json.hpp>

/* TODO: try to get ordered map working...
#include <tsl/ordered_map.h>
template<class Key, class T, class Ignore, class Allocator, 
         class Hash = std::hash<Key>, class KeyEqual = std::equal_to<Key>>
using ordered_map = tsl::ordered_map<Key, T, Hash, KeyEqual, Allocator>;

using json = nlohmann::basic_json<ordered_map>;
*/

// for convenience
using json = nlohmann::json;

class CudaNapi : public Napi::ObjectWrap<CudaNapi> {
  public:
    CudaNapi(const Napi::CallbackInfo&);
    Napi::Value Info(const Napi::CallbackInfo&);

    static Napi::Function GetClass(Napi::Env);

  private:
    std::string _hash;
    json _options;
};
