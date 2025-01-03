xlsxtools
=========

Utility functions for writing and manipulating Excel files:
- write_dataframe_to_excel() : write a Pandas DataFrame to an Excel file, optionally calling
    auto_size_excel_column_widths() and filter_and_freeze_excel()
- auto_size_excel_column_widths() : Reformat an Excel file, adjusting the column widths to fit their contents
- filter_and_freeze_excel() : Clean up an Excel file by setting a filter on the first row,
    splitting & freezing the panes


Releases
--------

0.1.0, 2021-10-26
* Initial release

0.2.0, 2025-01-02
* Move from pandas.ExcelWriter() to DataFrame.to_excel() (transparent to user)
* Add optional `tabname` argument to auto_size_excel_column_widths() and filter_and_freeze_excel()

License
-------

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.
