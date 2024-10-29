import subprocess
import os

def merge_pdfs(input_files, output_file):
    gs_command = [
        r'C:\Program Files\gs\gs10.04.0\bin\gswin64c.exe',
        '-dBATCH',
        '-dNOPAUSE',
        '-sDEVICE=pdfwrite',
        '-sOutputFile=' + output_file,
    ] + input_files
    try:
        subprocess.run(gs_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f'Fehler beim Zusammenführen der PDFs: {e}')

if __name__ == '__main__':
    pdfs_to_merge = [f"temps/temp_report_{i}.pdf" for i in range(24)]
    output_pdf = 'merged_output.pdf'
    pdfs_to_merge = [pdf for pdf in pdfs_to_merge if os.path.isfile(pdf)]
    if not pdfs_to_merge:
        print('Keine gültigen PDF-Dateien gefunden.')
    else:
        merge_pdfs(pdfs_to_merge, output_pdf)
