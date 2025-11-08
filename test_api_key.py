"""
Simple test script to verify API key validation
"""
from api_key_manager import validate_api_key

# Test cases
test_keys = [
    ("AIzaSyBeQC20FoxxHz-32VgjVgh_ew-OHK1ykqc", True, "Valid key"),
    ("AIza1234567890123456789012345678", True, "Valid format"),
    ("invalid_key", False, "Doesn't start with AIza"),
    ("AIza123", False, "Too short"),
    ("", False, "Empty key"),
    ("BIzaSyBeQC20FoxxHz-32VgjVgh_ew-OHK1ykqc", False, "Wrong prefix"),
]

print("🧪 Testing API Key Validation\n")
print("=" * 60)

for key, expected_valid, description in test_keys:
    is_valid, error_msg = validate_api_key(key)
    status = "✅ PASS" if is_valid == expected_valid else "❌ FAIL"
    
    print(f"\n{status} - {description}")
    print(f"   Key: {key[:20]}..." if len(key) > 20 else f"   Key: {key}")
    print(f"   Valid: {is_valid}")
    if error_msg:
        print(f"   Error: {error_msg}")

print("\n" + "=" * 60)
print("✅ All tests completed!")
