# BanglaKit Sentence Boundary Detector (SBD)

This simple Python Package detects the boundaries of Bengali sentences
and split sentences properly.

## Example

```python
import bengali_sbd

bengali_sbd.split('আমি বলেছিলাম, "ওখানে যাসনে। সাপ থাকতে পারে।" কেউ শুনল না।')
# [
#   'আমি বলেছিলাম, "ওখানে যাসনে। সাপ থাকতে পারে।"',
#   'কেউ শুনল না।'
# ]
```