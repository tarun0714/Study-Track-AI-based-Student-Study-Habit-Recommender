PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS Students (
  studentid INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS StudyLogs (
  logid INTEGER PRIMARY KEY,
  studentid INTEGER NOT NULL,
  date TEXT NOT NULL,
  studyhours REAL,
  methodused TEXT,
  distractions TEXT,
  quizscore REAL,
  FOREIGN KEY (studentid) REFERENCES Students(studentid) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Clusters (
  clusterid INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  averagestudyduration REAL,
  recommendedmethod TEXT,
  breakinterval INTEGER
);

CREATE TABLE IF NOT EXISTS Recommendations (
  recommendationid INTEGER PRIMARY KEY,
  studentid INTEGER NOT NULL,
  weeknumber INTEGER NOT NULL,
  recommendedhours REAL,
  suggestedmethod TEXT,
  tools TEXT,
  breakpattern TEXT,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (studentid) REFERENCES Students(studentid) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Feedback (
  feedbackid INTEGER PRIMARY KEY,
  studentid INTEGER NOT NULL,
  recommendationid INTEGER,
  adherence REAL,
  perceived_helpfulness INTEGER,
  comments TEXT,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (studentid) REFERENCES Students(studentid) ON DELETE CASCADE,
  FOREIGN KEY (recommendationid) REFERENCES Recommendations(recommendationid) ON DELETE SET NULL
);
