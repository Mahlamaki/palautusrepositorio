class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.score_player1 = 0
        self.score_player2 = 0


    def won_point(self, player_name):
        if player_name == self.player1_name :
            self.score_player1 +=1
        else:
            self.score_player2 +=1
        
    def get_draw_str(self,score):
        if self.score_player1  == 0:
            score = "Love-All"
        elif self.score_player1  == 1:
            score = "Fifteen-All"
        elif self.score_player1  == 2:
            score = "Thirty-All"
        else:
            score = "Deuce"
        return score
    
    def get_advantage_or_win(self,minus_result,score):
        if minus_result == 1:
            score = "Advantage player1"
        elif minus_result == -1:
            score = "Advantage player2"
        elif minus_result >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score
    
    def get_points_in_str(self,player_score):
        if player_score == 0:
            player_score = "Love"     
        elif player_score == 1:
            player_score = "Fifteen"
        elif player_score == 2:
            player_score = "Thirty"
        elif player_score == 3:
            player_score = "Forty"
        return player_score


    def get_score(self):
        score = ""
        score1 = ""
        score2 = ""

        if self.score_player1  == self.score_player2:
            score = self.get_draw_str(score)
            
        elif self.score_player1  >= 4 or self.score_player2 >= 4:
            minus_result = self.score_player1  - self.score_player2
            score = self.get_advantage_or_win(minus_result,score)


        else:
            score1 = self.get_points_in_str(self.score_player1)

            score2 = self.get_points_in_str(self.score_player2)
            score = f"{score1}-{score2}"

        return score

