from dao.watchlist_dao import WatchListDao

class WatchlistService:

    def remove_from_watchlist(self, watchlist_id):
        watchlist_dao = WatchListDao()
        delete_count = watchlist_dao.remove_from_watchlist(watchlist_id)
        return delete_count

    def update_status(self, user_id, movie_id, status):
        watchlist_dao = WatchListDao()
        update_count = watchlist_dao.update_status(user_id, movie_id, status)
        return update_count

    def get_watchlist(self, user_id):
       watchlist_dao = WatchListDao()
       rows = watchlist_dao.get_watchlist(user_id)
       return rows

    def save_in_watchlist(self, watchlist):

        watchlist_dao = WatchListDao()
        watchlist_dao.save_in_watchlist(watchlist)
