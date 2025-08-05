from dataclasses import dataclass, field


@dataclass
class PlayerStatus:
    score: int = field(init=True, default=0)
    lines: int = field(init=True, default=0)
    level: int = field(init=True, default=0)
    min_level: int = field(init=False, default=0)
    max_level: int = field(init=False, default=20)
    max_cleared_lines: int = field(init=False, default=4)
    base_scores: list = field(
        init=False, default_factory=lambda: [0, 40, 100, 300, 1200])

    def add_score(self, cleared_lines: int = 0):
        if cleared_lines > self.max_cleared_lines or cleared_lines < 0:
            raise ValueError('Wrong cleared lines: {}.'.format(cleared_lines))
        line_score = self.base_scores[cleared_lines] * (self.level + 1)
        self.score += line_score
        self.lines += cleared_lines

    def calculate_level(self):
        if self.level < self.max_level:
            self.level = self.lines // 10
        else:
            self.level = self.max_level