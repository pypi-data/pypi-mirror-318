class ReportGenerator:
    @staticmethod
    def create_report(result, format="pdf", include_graphs=True, include_recommendations=True):
        return {
            "format": format,
            "data": result.get_detailed_analysis(),
            "graphs": [] if include_graphs else None,
            "recommendations": result.recommendations if include_recommendations else None
        }
