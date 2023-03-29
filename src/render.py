import tempfile
import subprocess

def render_latex(latex_command, latex_data):
    with tempfile.TemporaryDirectory() as tmpdirname:
        # write latex data to a file
        with open(f"{tmpdirname}/resume.tex", "w") as f:
            f.write(latex_data)

        print(f"Wrote data to {tmpdirname}")

        # run latex command
        latex_process = subprocess.Popen(latex_command, cwd=tmpdirname)
        latex_process.wait()

        # read pdf data
        with open(f"{tmpdirname}/resume.pdf", "rb") as f:
            pdf_data = f.read()
        
        print(f"Read PDF data from {tmpdirname}")

    return pdf_data