class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
      aux_flowerbed = [0] + flowerbed + [0]
      new_flower_count = 0
      
      for i in range(1, len(aux_flowerbed) - 1):
        if aux_flowerbed[i-1] == 0 and aux_flowerbed[i+1] == 0 and aux_flowerbed[i] != 1:
          aux_flowerbed[i] = 1
          new_flower_count += 1
      
      return new_flower_count >= n