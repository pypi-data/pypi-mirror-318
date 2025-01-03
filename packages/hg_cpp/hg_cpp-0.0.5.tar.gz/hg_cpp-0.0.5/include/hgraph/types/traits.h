//
// Created by Howard Henson on 18/12/2024.
//

#ifndef TRAITS_H
#define TRAITS_H

#include <any>
#include <hgraph/python/pyb.h>
#include <optional>
#include <string>
#include <unordered_map>

namespace hgraph
{
    struct Traits : nb::intrusive_base
    {
        using ptr = nb::ref<Traits>;

        Traits() = default;

        explicit Traits(Traits::ptr parent_traits);

        void set_traits(nb::kwargs traits);

        [[nodiscard]] nb::object get_trait(const std::string &trait_name) const;

        [[nodiscard]] nb::object get_trait_or(const std::string &trait_name, nb::object &def_value) const;

        [[nodiscard]] Traits::ptr copy() const;

      private:
        std::optional<ptr> _parent_traits;
        nb::dict           _traits;
    };
}  // namespace hgraph

#endif  // TRAITS_H
