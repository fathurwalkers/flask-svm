-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Waktu pembuatan: 13 Jun 2023 pada 10.22
-- Versi server: 5.7.33
-- Versi PHP: 7.4.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `aplikasi_svm`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `bobot_kata`
--

CREATE TABLE `bobot_kata` (
  `id_bobot_kata` bigint(20) UNSIGNED NOT NULL,
  `kata` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `term_frequence` int(11) DEFAULT NULL,
  `idf` double(8,2) DEFAULT NULL,
  `tf_idf` double(8,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `crawling`
--

CREATE TABLE `crawling` (
  `id_crawling` bigint(20) UNSIGNED NOT NULL,
  `user_tweet` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `isi_tweet` longtext COLLATE utf8mb4_unicode_ci,
  `tanggal_tweet` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `login`
--

CREATE TABLE `login` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `login_nama` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `login_username` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `login_password` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `login_email` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `login_telepon` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `login_token` text COLLATE utf8mb4_unicode_ci,
  `login_level` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `login_status` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `login`
--

INSERT INTO `login` (`id`, `login_nama`, `login_username`, `login_password`, `login_email`, `login_telepon`, `login_token`, `login_level`, `login_status`, `created_at`, `updated_at`) VALUES
(1, 'Syarah', 'admin', '$2y$12$jELyhdfaj/JnSeZQIummpOYmuynqRvKLo1prdP342/R6TuvY9U2sa', 'administrator@pmb-unidayan.com', '085944923123', '$2y$12$A5.A0USW6lgM/5EB4ghWwehAiYu3vfthOnDaLA/iirtfR9n2bFSWy', 'admin', 'verified', '2023-06-13 00:47:26', '2023-06-13 00:47:26'),
(2, 'safar', 'safar', '$2y$12$8xbZMzYNL9P3hsdsUMeDvu8usFBNnWORTSdjwvCdsWNcAE4gUpnDK', 'safar@gmail.com', '085342442385', '$2y$12$Y7/da8O6gdmtlcqkemHd1uWRk379CIAfZjbJaR6rrT3cxOeSO9juG', 'admin', 'verified', '2023-06-13 00:47:27', '2023-06-13 00:47:27'),
(3, 'Fathur Walkers', 'fathurwalkers', '$2y$12$WRHYxdsC/pLpjydWReCvxOdy.1jhaqqzzpXvMgy8MLwVgH68Sd0vG', 'fathurwalkers@laravel.com', '084842848242', '$2y$12$aYvD4KwHDWOUWuhV9IyGyeIh.XLiMXYk78E3RwZV7b3tMtQbPMSKy', 'admin', 'verified', '2023-06-13 00:47:28', '2023-06-13 00:47:28'),
(4, 'Example Users', 'example', '$2y$12$u/pT0TlnXMYaEaNpIVNW9e2KEbuLnpcKF29TQvv9IbN2bq8Lyl.oW', 'user1@gmail.com', '085342072185', '$2y$12$MVPx40N4MB5ZlvOc2wRyb.RsBwroDxjR57rlOLjHx90HnEX/ywTAy', 'user', 'verified', '2023-06-13 00:47:29', '2023-06-13 00:47:29'),
(5, 'User 2', 'user2', '$2y$12$ENjpbH5/Sj7LdWRiJgfc2OPGDc2h96I.lF5pr0ZNp4xi80MVwR0.e', 'user2@gmail.com', '085342072185', '$2y$12$uThKEUtXTh6pm3y5BhbRgu1OQxq2jnxJmmPSeDaha1U553jPVDGUK', 'user', 'verified', '2023-06-13 00:47:29', '2023-06-13 00:47:29');

-- --------------------------------------------------------

--
-- Struktur dari tabel `migrations`
--

CREATE TABLE `migrations` (
  `id` int(10) UNSIGNED NOT NULL,
  `migration` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `batch` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `migrations`
--

INSERT INTO `migrations` (`id`, `migration`, `batch`) VALUES
(1, '2014_10_12_000000_create_users_table', 1),
(2, '2014_10_12_100000_create_password_resets_table', 1),
(3, '2019_08_19_000000_create_failed_jobs_table', 1),
(4, '2019_12_14_000001_create_personal_access_tokens_table', 1),
(5, '2023_06_12_091258_create_logins_table', 1),
(6, '2023_06_12_173108_create_crawlings_table', 1),
(7, '2023_06_12_173547_create_preprocessings_table', 1),
(8, '2023_06_12_174037_create_spellcorrections_table', 1),
(9, '2023_06_12_174248_create_bobotkatas_table', 1);

-- --------------------------------------------------------

--
-- Struktur dari tabel `preprocessing`
--

CREATE TABLE `preprocessing` (
  `id_preprocessing` bigint(20) UNSIGNED NOT NULL,
  `isi_tweet` longtext COLLATE utf8mb4_unicode_ci,
  `jumlah_kata` int(11) DEFAULT NULL,
  `jumlah_huruf` int(11) DEFAULT NULL,
  `jumlah_rerata_kata` int(11) DEFAULT NULL,
  `jumlah_stopword` int(11) DEFAULT NULL,
  `jumlah_hastag` int(11) DEFAULT NULL,
  `jumlah_karakter_numerik` int(11) DEFAULT NULL,
  `jumlah_uppercase` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `spellcorrection`
--

CREATE TABLE `spellcorrection` (
  `id_spellcorrection` bigint(20) UNSIGNED NOT NULL,
  `isi_tweet` longtext COLLATE utf8mb4_unicode_ci,
  `jumlah_kata` int(11) DEFAULT NULL,
  `jumlah_huruf` int(11) DEFAULT NULL,
  `jumlah_rerata_kata` int(11) DEFAULT NULL,
  `jumlah_stopword` int(11) DEFAULT NULL,
  `jumlah_hastag` int(11) DEFAULT NULL,
  `jumlah_karakter_numerik` int(11) DEFAULT NULL,
  `jumlah_uppercase` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `bobot_kata`
--
ALTER TABLE `bobot_kata`
  ADD PRIMARY KEY (`id_bobot_kata`);

--
-- Indeks untuk tabel `crawling`
--
ALTER TABLE `crawling`
  ADD PRIMARY KEY (`id_crawling`);

--
-- Indeks untuk tabel `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `login_login_username_unique` (`login_username`),
  ADD UNIQUE KEY `login_login_email_unique` (`login_email`);

--
-- Indeks untuk tabel `migrations`
--
ALTER TABLE `migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `preprocessing`
--
ALTER TABLE `preprocessing`
  ADD PRIMARY KEY (`id_preprocessing`);

--
-- Indeks untuk tabel `spellcorrection`
--
ALTER TABLE `spellcorrection`
  ADD PRIMARY KEY (`id_spellcorrection`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `bobot_kata`
--
ALTER TABLE `bobot_kata`
  MODIFY `id_bobot_kata` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `crawling`
--
ALTER TABLE `crawling`
  MODIFY `id_crawling` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `login`
--
ALTER TABLE `login`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT untuk tabel `migrations`
--
ALTER TABLE `migrations`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT untuk tabel `preprocessing`
--
ALTER TABLE `preprocessing`
  MODIFY `id_preprocessing` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `spellcorrection`
--
ALTER TABLE `spellcorrection`
  MODIFY `id_spellcorrection` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
