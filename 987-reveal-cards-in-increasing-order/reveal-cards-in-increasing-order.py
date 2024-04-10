class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:

        deck_sorted_desc = sorted(deck, reverse=True)
        ordered_deck = deque()

        for card in deck_sorted_desc:
            if len(ordered_deck) > 1:
                ordered_deck.rotate(1)
            ordered_deck.appendleft(card)
            #print(ordered_deck)

        return list(ordered_deck)



        
        
            
        