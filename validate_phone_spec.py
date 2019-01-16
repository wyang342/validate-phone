from mamba import description, context, it
from expects import expect, equal, be_true, be_false, be_none
from validate_phone import *

with description('#has_phone_number') as self:
    with it('finds the correct string'):
        expect(has_phone_number("my phone number: 111-222-3333")).to(be_true)
        expect(has_phone_number("please confirm your phone number: XXX-XXX-1234")).to(be_false)

with description('#get_phone_number') as self:
    with it('finds the correct string'):
        expect(get_phone_number("please don't share this: 999-888-1234")).to(equal("999-888-1234"))
        expect(get_phone_number("please confirm your phone number: XXX-XXX-1234")).to(be_none)

with description('#get_all_phone_numbers') as self:
    with it('finds the correct string'):
        expect(get_all_phone_numbers("234-609-1422, 350-802-0744,123-603-8762")).to(equal(["234-609-1422", "350-802-0744", "123-603-8762"]))
        expect(get_all_phone_numbers("please confirm your phone number: XXX-XXX-1422")).to(equal([]))

with description('#hide_phone_number') as self:
    with it('finds the correct string'):
        expect(hide_phone_number("234-620-1422, 350-830-0744, 123-603-8762")).to(equal("XXX-XXX-1422, XXX-XXX-0744, XXX-XXX-8762"))
        expect(hide_phone_number("please confirm your phone number: XXX-XXX-1422")).to(equal("please confirm your phone number: XXX-XXX-1422"))

with description('#format_phone_number') as self:
    with it('finds the correct string'):
        expect(format_phone_number("3112223333, 350.820.0744, 123-630-8762")).to(equal("311-222-3333, 350-820-0744, 123-630-8762"))
        expect(format_phone_number("please confirm your phone number: 421142233")).to(equal("please confirm your phone number: 421142233"))
