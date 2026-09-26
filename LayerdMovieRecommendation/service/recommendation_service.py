from dao.recommendation_dao import RecommendationDao

class RecommendationService:

    def get_recommendations(self, user_id):
        recommendation_dao = RecommendationDao()
        rows = recommendation_dao.get_recommendations(user_id)
        return rows