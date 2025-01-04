#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* nepopts.c */
/* Fortran interface file */

/*
* This file was generated automatically by bfort from the C source
* file.  
 */

#ifdef PETSC_USE_POINTER_CONVERSION
#if defined(__cplusplus)
extern "C" { 
#endif 
extern void *PetscToPointer(void*);
extern int PetscFromPointer(void *);
extern void PetscRmPointer(void*);
#if defined(__cplusplus)
} 
#endif 

#else

#define PetscToPointer(a) (a ? *(PetscFortranAddr *)(a) : 0)
#define PetscFromPointer(a) (PetscFortranAddr)(a)
#define PetscRmPointer(a)
#endif

#include "slepcnep.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepsetfromoptions_ NEPSETFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepsetfromoptions_ nepsetfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepgettolerances_ NEPGETTOLERANCES
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepgettolerances_ nepgettolerances
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepsettolerances_ NEPSETTOLERANCES
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepsettolerances_ nepsettolerances
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepgetdimensions_ NEPGETDIMENSIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepgetdimensions_ nepgetdimensions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepsetdimensions_ NEPSETDIMENSIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepsetdimensions_ nepsetdimensions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepsetwhicheigenpairs_ NEPSETWHICHEIGENPAIRS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepsetwhicheigenpairs_ nepsetwhicheigenpairs
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepgetwhicheigenpairs_ NEPGETWHICHEIGENPAIRS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepgetwhicheigenpairs_ nepgetwhicheigenpairs
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepsetproblemtype_ NEPSETPROBLEMTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepsetproblemtype_ nepsetproblemtype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepgetproblemtype_ NEPGETPROBLEMTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepgetproblemtype_ nepgetproblemtype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepsettwosided_ NEPSETTWOSIDED
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepsettwosided_ nepsettwosided
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepgettwosided_ NEPGETTWOSIDED
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepgettwosided_ nepgettwosided
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepsetconvergencetest_ NEPSETCONVERGENCETEST
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepsetconvergencetest_ nepsetconvergencetest
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepgetconvergencetest_ NEPGETCONVERGENCETEST
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepgetconvergencetest_ nepgetconvergencetest
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepsetstoppingtest_ NEPSETSTOPPINGTEST
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepsetstoppingtest_ nepsetstoppingtest
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepgetstoppingtest_ NEPGETSTOPPINGTEST
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepgetstoppingtest_ nepgetstoppingtest
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepsettrackall_ NEPSETTRACKALL
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepsettrackall_ nepsettrackall
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepgettrackall_ NEPGETTRACKALL
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepgettrackall_ nepgettrackall
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepsetrefine_ NEPSETREFINE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepsetrefine_ nepsetrefine
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepgetrefine_ NEPGETREFINE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepgetrefine_ nepgetrefine
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepsetoptionsprefix_ NEPSETOPTIONSPREFIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepsetoptionsprefix_ nepsetoptionsprefix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepappendoptionsprefix_ NEPAPPENDOPTIONSPREFIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepappendoptionsprefix_ nepappendoptionsprefix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepgetoptionsprefix_ NEPGETOPTIONSPREFIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepgetoptionsprefix_ nepgetoptionsprefix
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  nepsetfromoptions_(NEP nep, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPSetFromOptions(
	(NEP)PetscToPointer((nep) ));
}
SLEPC_EXTERN void  nepgettolerances_(NEP nep,PetscReal *tol,PetscInt *maxits, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLREAL(tol);
CHKFORTRANNULLINTEGER(maxits);
*ierr = NEPGetTolerances(
	(NEP)PetscToPointer((nep) ),tol,maxits);
}
SLEPC_EXTERN void  nepsettolerances_(NEP nep,PetscReal *tol,PetscInt *maxits, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPSetTolerances(
	(NEP)PetscToPointer((nep) ),*tol,*maxits);
}
SLEPC_EXTERN void  nepgetdimensions_(NEP nep,PetscInt *nev,PetscInt *ncv,PetscInt *mpd, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLINTEGER(nev);
CHKFORTRANNULLINTEGER(ncv);
CHKFORTRANNULLINTEGER(mpd);
*ierr = NEPGetDimensions(
	(NEP)PetscToPointer((nep) ),nev,ncv,mpd);
}
SLEPC_EXTERN void  nepsetdimensions_(NEP nep,PetscInt *nev,PetscInt *ncv,PetscInt *mpd, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPSetDimensions(
	(NEP)PetscToPointer((nep) ),*nev,*ncv,*mpd);
}
SLEPC_EXTERN void  nepsetwhicheigenpairs_(NEP nep,NEPWhich *which, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPSetWhichEigenpairs(
	(NEP)PetscToPointer((nep) ),*which);
}
SLEPC_EXTERN void  nepgetwhicheigenpairs_(NEP nep,NEPWhich *which, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPGetWhichEigenpairs(
	(NEP)PetscToPointer((nep) ),which);
}
SLEPC_EXTERN void  nepsetproblemtype_(NEP nep,NEPProblemType *type, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPSetProblemType(
	(NEP)PetscToPointer((nep) ),*type);
}
SLEPC_EXTERN void  nepgetproblemtype_(NEP nep,NEPProblemType *type, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPGetProblemType(
	(NEP)PetscToPointer((nep) ),type);
}
SLEPC_EXTERN void  nepsettwosided_(NEP nep,PetscBool *twosided, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPSetTwoSided(
	(NEP)PetscToPointer((nep) ),*twosided);
}
SLEPC_EXTERN void  nepgettwosided_(NEP nep,PetscBool *twosided, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPGetTwoSided(
	(NEP)PetscToPointer((nep) ),twosided);
}
SLEPC_EXTERN void  nepsetconvergencetest_(NEP nep,NEPConv *conv, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPSetConvergenceTest(
	(NEP)PetscToPointer((nep) ),*conv);
}
SLEPC_EXTERN void  nepgetconvergencetest_(NEP nep,NEPConv *conv, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPGetConvergenceTest(
	(NEP)PetscToPointer((nep) ),conv);
}
SLEPC_EXTERN void  nepsetstoppingtest_(NEP nep,NEPStop *stop, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPSetStoppingTest(
	(NEP)PetscToPointer((nep) ),*stop);
}
SLEPC_EXTERN void  nepgetstoppingtest_(NEP nep,NEPStop *stop, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPGetStoppingTest(
	(NEP)PetscToPointer((nep) ),stop);
}
SLEPC_EXTERN void  nepsettrackall_(NEP nep,PetscBool *trackall, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPSetTrackAll(
	(NEP)PetscToPointer((nep) ),*trackall);
}
SLEPC_EXTERN void  nepgettrackall_(NEP nep,PetscBool *trackall, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPGetTrackAll(
	(NEP)PetscToPointer((nep) ),trackall);
}
SLEPC_EXTERN void  nepsetrefine_(NEP nep,NEPRefine *refine,PetscInt *npart,PetscReal *tol,PetscInt *its,NEPRefineScheme *scheme, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPSetRefine(
	(NEP)PetscToPointer((nep) ),*refine,*npart,*tol,*its,*scheme);
}
SLEPC_EXTERN void  nepgetrefine_(NEP nep,NEPRefine *refine,PetscInt *npart,PetscReal *tol,PetscInt *its,NEPRefineScheme *scheme, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLINTEGER(npart);
CHKFORTRANNULLREAL(tol);
CHKFORTRANNULLINTEGER(its);
*ierr = NEPGetRefine(
	(NEP)PetscToPointer((nep) ),refine,npart,tol,its,scheme);
}
SLEPC_EXTERN void  nepsetoptionsprefix_(NEP nep, char *prefix, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(nep);
/* insert Fortran-to-C conversion for prefix */
  FIXCHAR(prefix,cl0,_cltmp0);
*ierr = NEPSetOptionsPrefix(
	(NEP)PetscToPointer((nep) ),_cltmp0);
  FREECHAR(prefix,_cltmp0);
}
SLEPC_EXTERN void  nepappendoptionsprefix_(NEP nep, char *prefix, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(nep);
/* insert Fortran-to-C conversion for prefix */
  FIXCHAR(prefix,cl0,_cltmp0);
*ierr = NEPAppendOptionsPrefix(
	(NEP)PetscToPointer((nep) ),_cltmp0);
  FREECHAR(prefix,_cltmp0);
}
SLEPC_EXTERN void  nepgetoptionsprefix_(NEP nep, char *prefix, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPGetOptionsPrefix(
	(NEP)PetscToPointer((nep) ),(const char **)&_cltmp0);
/* insert C-to-Fortran conversion for prefix */
*ierr = PetscStrncpy(prefix, _cltmp0, cl0);
                        if (*ierr) return;
                        FIXRETURNCHAR(PETSC_TRUE, prefix, cl0);
}
#if defined(__cplusplus)
}
#endif
