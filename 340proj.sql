DROP TABLE IF EXISTS `recipe_items`;

DROP TABLE IF EXISTS `settled`;

DROP TABLE IF EXISTS `materials`;

DROP TABLE IF EXISTS `furnitures`;

DROP TABLE IF EXISTS `musuems`;

DROP TABLE IF EXISTS `villagers`;

DROP TABLE IF EXISTS `islands`;

DROP TABLE IF EXISTS `users`;


CREATE TABLE `materials`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) DEFAULT NULL,
    `rarity` int(11) DEFAULT NULL,
    PRIMARY KEY(`id`),
    UNIQUE KEY `name` (`name`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO materials (name,rarity) VALUES 
(
    "Tree branch", '1'
),
(
    "Soft Wood", '1'
),
(
    "iron nuggets", '1'
),
(
    "Sagittarius fragment", '5'
);

CREATE TABLE `furnitures`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(255) NOT NULL,
    `size` int(11) DEFAULT '0',
    `sold` int(11) DEFAULT '-1',
    `bought`  int(11) DEFAULT '-1',
    `source` int(11) DEFAULT '0',
    `customizable` int(11) DEFAULT '-1',
    PRIMARY KEY (`id`),
    UNIQUE KEY `name` (`name`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO furnitures(name,size,sold,bought,source,customizable) VALUES
(
    "Air circulator", '0', '275', '1100', '0', '-1'
),
(
    "Acoustic guitar", '0', '3210', '-1', '1', '5'
);


CREATE TABLE `recipe_items`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `fid` int(11) NOT NULL DEFAULT '0',
    `mid` int(11) NOT NULL,
    `number` int(11) NOT NULL DEFAULT '0',
    PRIMARY KEY (`id`),
    KEY `idx_receipe_fk1` (`fid`),
    KEY `idx_receipe_fk2` (`mid`),
    CONSTRAINT `receipe_fk1` FOREIGN KEY (`fid`) REFERENCES `furnitures` (`id`),
    CONSTRAINT `receipe_fk2` FOREIGN KEY (`mid`) REFERENCES `materials` (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO recipe_items(fid, mid, number) VALUES
(
    '2', '2', '8'
),
(
    '2', '3', '3'
);

-- CREATE TABLE `musuems`(
--     `id` int(11) NOT NULL AUTO_INCREMENT,
--     `name` VARCHAR(255),

-- )

CREATE TABLE `villagers`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `phrase` VARCHAR(255) DEFAULT NULL,
    `gender` int(11) DEFAULT NULL,
    `personality` int(11) DEFAULT NULL,
    `species` int(11) DEFAULT NULL,
    `clothes` int(11) DEFAULT NULL,
    `birthday` varchar(255) DEFAULT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `name` (`name`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO villagers (name, phrase, gender, personality, species, clothes, birthday) VALUES
(
    "Admiral", "aye aye", '0', '2', '4', NULL, "01-27"
),
(
    "Antonio", "honk", '0', '1', '0', NULL, "10-20"
);


CREATE TABLE `users`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    PRIMARY KEY(`id`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO users (name) VALUES
(
    "test_user"
);

CREATE TABLE `islands`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `uid` int(11) NOT NULL,
    PRIMARY KEY (`id`),
    KEY `idx_island_fk1` (`uid`),
    CONSTRAINT `island_fk1` FOREIGN KEY (`uid`) REFERENCES `users` (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO islands(name, uid) VALUES
(
    "test_island", '1'
);

CREATE TABLE `settled`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `vid` int(11) NOT NULL,
    `iid` int(11) NOT NULL,
    PRIMARY KEY(`id`),
    KEY `idx_settled_fk1`(`vid`),
    KEY `idx_settled_fk2`(`iid`),
    CONSTRAINT `settled_fk1` FOREIGN KEY(`vid`) REFERENCES `villagers` (`id`),
    CONSTRAINT `settled_fk2` FOREIGN KEY(`iid`) REFERENCES `islands` (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO settled(vid, iid) VALUES
(
    '1', '1' 
),
(
    '2', '1'
);