"""
This is a boilerplate pipeline 'mdp'
generated using Kedro 0.17.6
"""

from kedro.pipeline import Pipeline, node

from .nodes import tratamento


def create_pipeline(**kwargs) -> Pipeline:
    r""" "
    transformacao create_pipeline
    """
    pipeline_limpeza = Pipeline(
        [
            node(
                tratamento,
                inputs="estacoes",
                outputs="estacoes_limpa",
                name="node_limpeza",
            )
        ]
    )

    return pipeline_limpeza
