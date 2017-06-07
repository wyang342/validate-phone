require_relative 'validate_phone'

describe "#has_phone_number? tests" do
  it "returns true if it has a string that appears to be a phone number" do
    expect(has_phone_number?("my phone number: 111-222-3333")).to eq(true)
  end

  it "returns false if it does not have a phone number" do
    expect(has_phone_number?("please confirm your phone number: XXX-XXX-1234")).to eq(false)
  end
end

describe "#get_phone_number tests" do
  it "returns a phone number if the string has an phone number" do
    expect(get_phone_number("please don't share this: 999-888-1234")).to eq("999-888-1234")
  end

  it "returns nil if it doesn't have a phone number" do
    expect(get_phone_number("please confirm your phone number: XXX-XXX-1234")).to eq(nil)
  end
end

describe "#get_all_phone_numbers" do
  it "returns all phone numbers if the string has any phone numbers" do
    expect(get_all_phone_numbers("234-609-1422, 350-802-0744, 123-603-8762")).to eq(["234-609-1422", "350-802-0744", "123-603-8762"])
  end

  it "get_all_phone_numbers numbers returns an empty Array if it doesn't have any phone numbers" do
    expect(get_all_phone_numbers("please confirm your phone number: XXX-XXX-1422")).to eq([])
  end
end

describe "#hide_phone_numbers numbers" do
  it "obfuscates any phone numbers in the string" do
    expect(hide_phone_numbers("234-620-1422, 350-830-0744, 123-603-8762")).to eq("XXX-XXX-1422, XXX-XXX-0744, XXX-XXX-8762")
  end

  it "does not alter a string without phone numbers in it" do
    string = "please confirm your phone number: XXX-XXX-1422"
    expect(hide_phone_numbers(string)).to eq(string)
  end
end

describe "#format_phone_number" do
  it "finds and reformat any phone numbers in the string" do
    expect(format_phone_number("3112223333, 350.820.0744, 123-630-8762")).to eq("311-222-3333, 350-820-0744, 123-630-8762")
  end

  it "does not alter a string without phone numbers in it" do
    string = "please confirm your phone number: 4421142233"
    expect(format_phone_number(string)).to eq(string)
  end
end
