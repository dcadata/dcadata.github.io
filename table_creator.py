cell_with_image_format = '[![{0}]({1})]({2})'
cell_without_image_format = '[**{0}**]({2})'
row_format = '|{}|{}|{}|'
header_format = '\n'.join((
    '| | | |',
    '|:------:|:------:|:------:|',
))

begin_marker = '<!-- BEGIN HIGHLIGHTS -->\n\n'
end_marker = '\n\n<!-- END HIGHLIGHTS -->'

files_to_update = (
    'index.md',
    '404.md',
    'preview.md',
)

order_text = open('table_order.txt').read()
records = [section.split('\n') for section in order_text.split('\n\n')]

record_batches = [records[idx:idx + 3] for idx in range(0, len(records), 3)]

formatted = ['\n'.join((
    row_format.format(*[cell_with_image_format.format(*i) for i in batch]),
    row_format.format(*[cell_without_image_format.format(*i) for i in batch]),
)) for batch in record_batches]
formatted_text = '\n\n'.join(formatted)

for file_to_update in files_to_update:
    old_text = open(file_to_update).read()
    beginning_text = old_text.split(begin_marker, 1)[0]
    end_text = old_text.rsplit(end_marker, 1)[1]
    updated_text = ''.join((
        beginning_text,
        begin_marker,
        formatted_text,
        end_marker,
        end_text,
    ))
    open(file_to_update, 'w').write(updated_text)
