FROM continuumio/miniconda3:latest

WORKDIR /app

COPY MLProject/ /app/MLProject/

RUN conda env create -f /app/MLProject/conda.yaml &&     conda clean -afy

SHELL ["conda", "run", "-n", "mlops-env", "/bin/bash", "-c"]

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "mlops-env", "python", "/app/MLProject/modelling.py"]
